from .theme import make_theme

OCEANIC_THEME = make_theme(
    fontname='Arial',
    graph_bgcolor='#22356f', graph_fontcolor='#e0f7fa',
    label_bgcolor='#4fd3c4',
    edge_color='#1976d2',
    node_fillcolor='#4fd3c4', node_fontcolor='#22356f',
    start_fillcolor='#1976d2', start_fontcolor='#e0f7fa',
    end_fillcolor='#e0f7fa', end_fontcolor='#22356f',
    error_fillcolor='#ff5252', error_fontcolor='#e0f7fa', error_edge_color='#ff5252',
    warn_fillcolor='#ffd740', warn_fontcolor='#22356f', warn_edge_color='#ffd740',
    info_fillcolor='#4fd3c4', info_fontcolor='#22356f', info_edge_color='#4fd3c4',
    service_colors=[
        ("#4fd3c4", "#22356f"),
        ("#1976d2", "#e0f7fa"),
        ("#e0f7fa", "#22356f"),
        ("#ffd740", "#22356f"),
        ("#ff5252", "#e0f7fa"),
    ],
    group_colors=[
        ("#22356f", "#e0f7fa"),
        ("#4fd3c4", "#22356f"),
        ("#1976d2", "#e0f7fa"),
        ("#e0f7fa", "#22356f"),
    ],
)
