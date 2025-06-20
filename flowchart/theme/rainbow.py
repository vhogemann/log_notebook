# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

RAINBOW_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#ffffff',
        fontcolor='#222222',
        fontname='Arial',
    ),
    label=GraphLabelStyle(
        fontname='Arial',
        fontsize='14',
        bgcolor='#ff0000',
    ),
    edge=EdgeStyle(
        color='#222222',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#ff0000',
        fontname='Arial',
        fontsize='14',
        fontcolor='#ffffff',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#ff9900",
        fontname='Arial',
        fontsize='14',
        fontcolor='#ffffff',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#33cc33',
        fontname='Arial',
        fontsize='14',
        fontcolor='#ffffff',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#6600cc',
        fontname='Arial',
        fontsize='10',
        fontcolor='#ffffff',
    ),
    error_edge=EdgeStyle(
        color='#6600cc',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffcc00',
        fontname='Arial',
        fontsize='10',
        fontcolor='#222222',
    ),
    warn_edge=EdgeStyle(
        color='#ffcc00',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#0099ff',
        fontname='Arial',
        fontsize='10',
        fontcolor='#ffffff',
    ),
    info_edge=EdgeStyle(
        color='#0099ff',
        style='dashed',
    ),
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
    ]
)
