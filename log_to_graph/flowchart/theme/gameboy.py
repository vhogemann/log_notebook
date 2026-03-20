from .theme import make_theme

GAMEBOY_THEME = make_theme(
    fontname='Courier New',
    graph_bgcolor='#9bbc0f', graph_fontcolor='#0f380f',
    label_bgcolor='#8bac0f',
    edge_color='#306230',
    node_fillcolor='#8bac0f', node_fontcolor='#0f380f',
    start_fillcolor='#306230', start_fontcolor='#e0f8d0',
    end_fillcolor='#0f380f', end_fontcolor='#e0f8d0',
    error_fillcolor='#e0f8d0', error_fontcolor='#0f380f', error_edge_color='#e0f8d0',
    warn_fillcolor='#8bac0f', warn_fontcolor='#0f380f', warn_edge_color='#8bac0f',
    info_fillcolor='#9bbc0f', info_fontcolor='#0f380f', info_edge_color='#9bbc0f',
    service_colors=[
        ("#8bac0f", "#0f380f"),
        ("#306230", "#e0f8d0"),
        ("#0f380f", "#e0f8d0"),
        ("#e0f8d0", "#0f380f"),
    ],
    group_colors=[
        ("#9bbc0f", "#0f380f"),
        ("#8bac0f", "#0f380f"),
        ("#306230", "#e0f8d0"),
        ("#0f380f", "#e0f8d0"),
    ],
)
