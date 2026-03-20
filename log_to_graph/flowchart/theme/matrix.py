from .theme import make_theme

MATRIX_THEME = make_theme(
    fontname='Consolas',
    graph_bgcolor='#000000', graph_fontcolor='#00ff41',
    label_bgcolor='#003b00',
    edge_color='#00ff41',
    node_fillcolor='#003b00', node_fontcolor='#00ff41',
    start_fillcolor='#00ff41', start_fontcolor='#000000',
    end_fillcolor='#003b00', end_fontcolor='#00ff41',
    error_fillcolor='#ff0000', error_fontcolor='#00ff41', error_edge_color='#ff0000',
    warn_fillcolor='#ffff00', warn_fontcolor='#003b00', warn_edge_color='#ffff00',
    info_fillcolor='#003b00', info_fontcolor='#00ff41', info_edge_color='#00ff41',
    service_colors=[
        ("#003b00", "#00ff41"),
        ("#00ff41", "#000000"),
        ("#000000", "#00ff41"),
        ("#ff0000", "#00ff41"),
        ("#ffff00", "#003b00"),
    ],
    group_colors=[
        ("#000000", "#00ff41"),
        ("#003b00", "#00ff41"),
        ("#00ff41", "#000000"),
        ("#ff0000", "#00ff41"),
    ],
)
