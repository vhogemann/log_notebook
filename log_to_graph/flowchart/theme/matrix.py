# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

MATRIX_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#000000',
        fontcolor='#00ff41',
        fontname='Consolas',
    ),
    label=GraphLabelStyle(
        fontname='Consolas',
        fontsize='14',
        bgcolor='#003b00',
    ),
    edge=EdgeStyle(
        color='#00ff41',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#003b00',
        fontname='Consolas',
        fontsize='14',
        fontcolor='#00ff41',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#00ff41",
        fontname='Consolas',
        fontsize='14',
        fontcolor='#000000',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#003b00',
        fontname='Consolas',
        fontsize='14',
        fontcolor='#00ff41',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ff0000',
        fontname='Consolas',
        fontsize='10',
        fontcolor='#00ff41',
    ),
    error_edge=EdgeStyle(
        color='#ff0000',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffff00',
        fontname='Consolas',
        fontsize='10',
        fontcolor='#003b00',
    ),
    warn_edge=EdgeStyle(
        color='#ffff00',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#003b00',
        fontname='Consolas',
        fontsize='10',
        fontcolor='#00ff41',
    ),
    info_edge=EdgeStyle(
        color='#00ff41',
        style='dashed',
    ),
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
    ]
)
