from .theme import make_theme

CYBERPUNK_THEME = make_theme(
    fontname='Arial',
    graph_bgcolor='#18181a', graph_fontcolor='#ff00c8',
    label_bgcolor='#00fff7',
    edge_color='#ffea00',
    node_fillcolor='#ff00c8', node_fontcolor='#18181a',
    start_fillcolor='#00fff7', start_fontcolor='#18181a',
    end_fillcolor='#ffea00', end_fontcolor='#18181a',
    error_fillcolor='#ff003c', error_fontcolor='#00fff7', error_edge_color='#ff003c',
    warn_fillcolor='#ffea00', warn_fontcolor='#18181a', warn_edge_color='#ffea00',
    info_fillcolor='#00fff7', info_fontcolor='#18181a', info_edge_color='#00fff7',
    service_colors=[
        ("#ff00c8", "#18181a"),
        ("#00fff7", "#18181a"),
        ("#ffea00", "#18181a"),
        ("#ff003c", "#00fff7"),
        ("#18181a", "#ff00c8"),
    ],
    group_colors=[
        ("#18181a", "#ff00c8"),
        ("#00fff7", "#18181a"),
        ("#ffea00", "#18181a"),
        ("#ff00c8", "#18181a"),
    ],
)
