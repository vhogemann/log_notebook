# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

OCEANIC_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#22356f',
        fontcolor='#e0f7fa',
        fontname='Arial',
    ),
    label=GraphLabelStyle(
        fontname='Arial',
        fontsize='14',
        bgcolor='#4fd3c4',
    ),
    edge=EdgeStyle(
        color='#1976d2',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#4fd3c4',
        fontname='Arial',
        fontsize='14',
        fontcolor='#22356f',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#1976d2",
        fontname='Arial',
        fontsize='14',
        fontcolor='#e0f7fa',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#e0f7fa',
        fontname='Arial',
        fontsize='14',
        fontcolor='#22356f',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ff5252',
        fontname='Arial',
        fontsize='10',
        fontcolor='#e0f7fa',
    ),
    error_edge=EdgeStyle(
        color='#ff5252',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffd740',
        fontname='Arial',
        fontsize='10',
        fontcolor='#22356f',
    ),
    warn_edge=EdgeStyle(
        color='#ffd740',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#4fd3c4',
        fontname='Arial',
        fontsize='10',
        fontcolor='#22356f',
    ),
    info_edge=EdgeStyle(
        color='#4fd3c4',
        style='dashed',
    ),
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
    ]
)
