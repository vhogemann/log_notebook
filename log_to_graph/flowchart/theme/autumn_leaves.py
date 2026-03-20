from .theme import make_theme

AUTUMN_LEAVES_THEME = make_theme(
    fontname='Georgia',
    graph_bgcolor='#fff8e1', graph_fontcolor='#a0522d',
    label_bgcolor='#ffb347',
    edge_color='#d2691e',
    node_fillcolor='#ffb347', node_fontcolor='#a0522d',
    start_fillcolor='#ff6961', start_fontcolor='#fff8e1',
    end_fillcolor='#c2b280', end_fontcolor='#a0522d',
    error_fillcolor='#ff6961', error_fontcolor='#fff8e1', error_edge_color='#ff6961',
    warn_fillcolor='#ffb347', warn_fontcolor='#a0522d', warn_edge_color='#ffb347',
    info_fillcolor='#c2b280', info_fontcolor='#a0522d', info_edge_color='#c2b280',
    service_colors=[
        ("#ffb347", "#a0522d"),
        ("#ff6961", "#fff8e1"),
        ("#c2b280", "#a0522d"),
        ("#fff8e1", "#a0522d"),
        ("#d2691e", "#fff8e1"),
    ],
    group_colors=[
        ("#fff8e1", "#a0522d"),
        ("#ffb347", "#a0522d"),
        ("#ff6961", "#fff8e1"),
        ("#c2b280", "#a0522d"),
    ],
)
