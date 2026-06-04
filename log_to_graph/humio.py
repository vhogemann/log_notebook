import os
import random
import time
import json
import uuid
import tempfile
from typing import Optional, Tuple

from humiolib.HumioClient import HumioClient
from humiolib.HumioExceptions import HumioConnectionException, HumioTimeoutException


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _env_float(name: str, default: float) -> float:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return default


def _resolve_timeout(http_timeout: Optional[Tuple[float, float]]) -> Tuple[float, float]:
    if http_timeout is not None:
        return http_timeout
    connect_timeout = _env_float("HUMIO_CONNECT_TIMEOUT_SECONDS", 5.0)
    read_timeout = _env_float("HUMIO_READ_TIMEOUT_SECONDS", 30.0)
    return (connect_timeout, read_timeout)


def _retry_delay(base_delay: float, max_delay: float, attempt: int) -> float:
    # Add small jitter to avoid synchronized retries.
    return min(base_delay * (2 ** attempt), max_delay) + random.uniform(0.0, 0.25)


def _stream_query_to_njson(
    user_token: str,
    repo: str,
    start: str,
    query: str,
    output_filename: str,
    base_url: Optional[str] = None,
    http_timeout: Optional[Tuple[float, float]] = None,
    max_retries: Optional[int] = None,
    backoff_seconds: Optional[float] = None,
    max_backoff_seconds: Optional[float] = None,
) -> None:
    """Run a Humio query and stream events to a .njson file (raises on error)."""
    resolved_base_url = base_url or os.getenv("HUMIO_BASE_URL", "https://cloud.humio.com")
    resolved_timeout = _resolve_timeout(http_timeout)
    resolved_retries = max_retries if max_retries is not None else _env_int("HUMIO_MAX_RETRIES", 4)
    resolved_backoff = backoff_seconds if backoff_seconds is not None else _env_float("HUMIO_BACKOFF_SECONDS", 0.5)
    resolved_max_backoff = (
        max_backoff_seconds
        if max_backoff_seconds is not None
        else _env_float("HUMIO_MAX_BACKOFF_SECONDS", 8.0)
    )

    client = HumioClient(
        base_url=resolved_base_url,
        repository=repo,
        user_token=user_token
    )
    queryjob = client.create_queryjob(query, is_live=False, start=start, timeout=resolved_timeout)

    with open(output_filename, "w", encoding="utf-8") as f:
        while queryjob.more_segments_can_be_polled:
            for attempt in range(resolved_retries + 1):
                try:
                    poll_result = queryjob.poll(timeout=resolved_timeout)
                    for event in poll_result.events:
                        # NJSON/NDJSON: one JSON object per line.
                        f.write(json.dumps(event, ensure_ascii=False) + "\n")
                    f.flush()
                    break
                except (HumioConnectionException, HumioTimeoutException):
                    if attempt >= resolved_retries:
                        raise
                    time.sleep(_retry_delay(resolved_backoff, resolved_max_backoff, attempt))


def _read_njson_events(filename: str) -> list:
    """Load line-delimited JSON objects from a .njson file."""
    events = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            events.append(json.loads(line))
    return events


def query(
    user_token: str,
    repo: str,
    start: str,
    query: str,
    base_url: Optional[str] = None,
    http_timeout: Optional[Tuple[float, float]] = None,
    max_retries: Optional[int] = None,
    backoff_seconds: Optional[float] = None,
    max_backoff_seconds: Optional[float] = None,
) -> list:
    temp_filename = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}.njson")
    completed = False

    try:
        _stream_query_to_njson(
            user_token=user_token,
            repo=repo,
            start=start,
            query=query,
            output_filename=temp_filename,
            base_url=base_url,
            http_timeout=http_timeout,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
            max_backoff_seconds=max_backoff_seconds,
        )
        completed = True

        event_list = _read_njson_events(temp_filename)
        event_list.sort(key=lambda x: x.get("timestamp", ""))
        return event_list
    finally:
        # Keep partial results on disk if the query failed.
        if completed:
            try:
                os.remove(temp_filename)
            except OSError:
                pass


def query_logs(
    user_token: str,
    repo: str,
    start: str,
    correlation_id: str,
    base_url: Optional[str] = None,
    http_timeout: Optional[Tuple[float, float]] = None,
    max_retries: Optional[int] = None,
    backoff_seconds: Optional[float] = None,
    max_backoff_seconds: Optional[float] = None,
) -> dict[str, list]:
    """
    Query logs from Humio repository based on correlation_id.
    
    :param user_token: The Humio user token for authentication.
    :param repo: The Humio repository to query.
    :param start: The start time for the query, e.g., "12h" for the last 12 hours.
    :param correlation_id: The correlation ID to filter logs.
    :return: A dictionary of events matching the correlation ID.
    """
    
    event_list = query(
        user_token,
        repo,
        start,
        f" join({{{correlation_id} class=* service=*}}, field=correlation_id)",
        base_url=base_url,
        http_timeout=http_timeout,
        max_retries=max_retries,
        backoff_seconds=backoff_seconds,
        max_backoff_seconds=max_backoff_seconds,
    )
    event_map: dict[str, list] = {}

    for event in event_list:
        corr_id = event.get("correlation_id")
        if not corr_id:
            continue
        if corr_id not in event_map:
            event_map[corr_id] = []
        event_map[corr_id].append(event)

    return event_map


def query_to_njson(
    user_token: str,
    repo: str,
    start: str,
    query: str,
    base_url: Optional[str] = None,
    http_timeout: Optional[Tuple[float, float]] = None,
    max_retries: Optional[int] = None,
    backoff_seconds: Optional[float] = None,
    max_backoff_seconds: Optional[float] = None,
    filename: Optional[str] = None,
) -> tuple[str, int]:
    """Run a Humio query and stream events to a .njson file.

    Returns (filename, status_code) where status_code is:
    - 0 on success
    - 1 on error (partial data may already be persisted)
    """
    output_filename = filename or f"{uuid.uuid4()}.njson"

    try:
        _stream_query_to_njson(
            user_token=user_token,
            repo=repo,
            start=start,
            query=query,
            output_filename=output_filename,
            base_url=base_url,
            http_timeout=http_timeout,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
            max_backoff_seconds=max_backoff_seconds,
        )
        return output_filename, 0
    except Exception:
        return output_filename, 1
