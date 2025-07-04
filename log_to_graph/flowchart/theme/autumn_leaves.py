# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

AUTUMN_LEAVES_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#fff8e1',
        fontcolor='#a0522d',
        fontname='Georgia',
    ),
    label=GraphLabelStyle(
        fontname='Georgia',
        fontsize='14',
        bgcolor='#ffb347',
    ),
    edge=EdgeStyle(
        color='#d2691e',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#ffb347',
        fontname='Georgia',
        fontsize='14',
        fontcolor='#a0522d',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#ff6961",
        fontname='Georgia',
        fontsize='14',
        fontcolor='#fff8e1',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#c2b280',
        fontname='Georgia',
        fontsize='14',
        fontcolor='#a0522d',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ff6961',
        fontname='Georgia',
        fontsize='10',
        fontcolor='#fff8e1',
    ),
    error_edge=EdgeStyle(
        color='#ff6961',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffb347',
        fontname='Georgia',
        fontsize='10',
        fontcolor='#a0522d',
    ),
    warn_edge=EdgeStyle(
        color='#ffb347',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#c2b280',
        fontname='Georgia',
        fontsize='10',
        fontcolor='#a0522d',
    ),
    info_edge=EdgeStyle(
        color='#c2b280',
        style='dashed',
    ),
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
    ]
)
