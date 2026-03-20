from .theme import make_theme

RAINBOW_THEME = make_theme(
    fontname='Arial',
    graph_bgcolor='#ffffff', graph_fontcolor='#222222',
    label_bgcolor='#ff0000',
    edge_color='#222222',
    node_fillcolor='#ff0000', node_fontcolor='#ffffff',
    start_fillcolor='#ff9900', start_fontcolor='#ffffff',
    end_fillcolor='#33cc33', end_fontcolor='#ffffff',
    error_fillcolor='#6600cc', error_fontcolor='#ffffff', error_edge_color='#6600cc',
    warn_fillcolor='#ffcc00', warn_fontcolor='#222222', warn_edge_color='#ffcc00',
    info_fillcolor='#0099ff', info_fontcolor='#ffffff', info_edge_color='#0099ff',
    service_colors=[
        ("#ff0000", "#ffffff"),
        ("#ff9900", "#ffffff"),
        ("#ffcc00", "#222222"),
        ("#33cc33", "#ffffff"),
        ("#0099ff", "#ffffff"),
        ("#6600cc", "#ffffff"),
        ("#ff66cc", "#222222"),
    ],
    group_colors=[
        ("#ff0000", "#ffffff"),
        ("#ff9900", "#ffffff"),
        ("#ffcc00", "#222222"),
        ("#33cc33", "#ffffff"),
        ("#0099ff", "#ffffff"),
        ("#6600cc", "#ffffff"),
        ("#ff66cc", "#222222"),
    ],
)
