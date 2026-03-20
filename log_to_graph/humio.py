from humiolib.HumioClient import HumioClient

def query(user_token:str, repo:str, start:str, query:str) -> list:
    client = HumioClient(
        base_url="https://cloud.humio.com",
        repository=repo,
        user_token=user_token
    )
    queryjob = client.create_queryjob(query, is_live=False, start=start)
    event_list = []
    for poll_result in queryjob.poll_until_done():
        for event in poll_result.events:
            event_list.append(event)

    event_list.sort(key=lambda x: x.get("timestamp",""))

    return event_list


def query_logs(user_token:str, repo:str, start:str, correlation_id:str) -> dict[str,list]:
    """
    Query logs from Humio repository based on correlation_id.
    
    :param user_token: The Humio user token for authentication.
    :param repo: The Humio repository to query.
    :param start: The start time for the query, e.g., "12h" for the last 12 hours.
    :param correlation_id: The correlation ID to filter logs.
    :return: A dictionary of events matching the correlation ID.
    """
    
    event_list = query(user_token, repo, start, f" join({{{correlation_id} class=* service=*}}, field=correlation_id)")
    event_map: dict[str,list] = {}

    for event in event_list:
        if event["correlation_id"] not in event_map:
            event_map[event["correlation_id"]] = []
        event_map[event["correlation_id"]].append(event)

    return event_map