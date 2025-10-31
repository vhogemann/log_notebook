"""
Backend logic for the Streamlit web interface.
Handles Humio queries and flowchart generation.
"""
from typing import Optional
from log_to_graph.humio import query_logs
from log_to_graph.flowchart import node_factory, FlowChart
from log_to_graph.flowchart.theme import Theme


def generate_flowchart_svg(
    user_token: str,
    repo: str,
    start: str,
    correlation_id: str,
    theme: Theme
) -> Optional[str]:
    """
    Query Humio logs and generate a flowchart SVG.

    Args:
        user_token: Humio API token for authentication
        repo: Humio repository name
        start: Time range for query (e.g., "3h", "1d", "7d")
        correlation_id: Correlation ID to filter logs
        theme: Theme object for flowchart styling

    Returns:
        SVG string if successful, None if no events found

    Raises:
        Exception: If query fails or other errors occur
    """
    # Query logs from Humio
    event_map = query_logs(user_token, repo, start, correlation_id)

    if not event_map:
        return None

    # Get the first correlation ID's events
    correlation_id_list = list(event_map.keys())
    if not correlation_id_list:
        return None

    first_correlation_id = correlation_id_list[0]
    events = event_map[first_correlation_id]

    if not events:
        return None

    # Create nodes from events
    nodes = [node_factory(event) for event in events]

    # Generate flowchart
    flowchart = FlowChart(first_correlation_id, nodes, theme=theme)

    # Generate SVG using graphviz
    dot = flowchart.to_graphviz()

    # Render to SVG string
    svg_string = dot.pipe(format='svg').decode('utf-8')

    return svg_string
