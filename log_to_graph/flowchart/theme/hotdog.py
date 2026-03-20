from .theme import make_theme

HOTDOG_THEME = make_theme(
    fontname='Courier New',
    graph_bgcolor='#ffffff', graph_fontcolor='#000000',
    label_bgcolor='#ff0000',
    edge_color='#000000',
    node_fillcolor='#ffcc00', node_fontcolor='#000000',
    start_fillcolor='#ff0000', start_fontcolor='#ffffff',
    end_fillcolor='#000000', end_fontcolor='#ffcc00',
    error_fillcolor='#ff0000', error_fontcolor='#ffffff', error_edge_color='#ff0000',
    warn_fillcolor='#ffcc00', warn_fontcolor='#000000', warn_edge_color='#ffcc00',
    info_fillcolor='#ffffff', info_fontcolor='#000000', info_edge_color='#000000',
    service_colors=[
        ("#ffcc00", "#000000"),
        ("#ff0000", "#ffffff"),
        ("#000000", "#ffcc00"),
        ("#ffffff", "#ff0000"),
        ("#000000", "#ffffff"),
        ("#ffffff", "#000000"),
        ("#ffcc00", "#ff0000"),
        ("#ff0000", "#ffcc00"),
    ],
    group_colors=[
        ("#ffffff", "#000000"),
        ("#ffcc00", "#000000"),
        ("#ff0000", "#ffffff"),
        ("#000000", "#ffcc00"),
        ("#ffcc00", "#ff0000"),
        ("#ff0000", "#ffcc00"),
        ("#000000", "#ffffff"),
        ("#ffffff", "#ff0000"),
    ],
)
