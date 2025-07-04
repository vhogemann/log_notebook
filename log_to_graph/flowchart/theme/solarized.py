# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

SOLARIZED_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#fdf6e3',
        fontcolor='#657b83',
        fontname='Fira Mono',
    ),
    label=GraphLabelStyle(
        fontname='Fira Mono',
        fontsize='14',
        bgcolor='#eee8d5',
    ),
    edge=EdgeStyle(
        color='#b58900',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#b58900',
        fontname='Fira Mono',
        fontsize='14',
        fontcolor='#fdf6e3',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#2aa198",
        fontname='Fira Mono',
        fontsize='14',
        fontcolor='#fdf6e3',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#268bd2',
        fontname='Fira Mono',
        fontsize='14',
        fontcolor='#fdf6e3',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#dc322f',
        fontname='Fira Mono',
        fontsize='10',
        fontcolor='#fdf6e3',
    ),
    error_edge=EdgeStyle(
        color='#dc322f',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#b58900',
        fontname='Fira Mono',
        fontsize='10',
        fontcolor='#fdf6e3',
    ),
    warn_edge=EdgeStyle(
        color='#b58900',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#2aa198',
        fontname='Fira Mono',
        fontsize='10',
        fontcolor='#fdf6e3',
    ),
    info_edge=EdgeStyle(
        color='#2aa198',
        style='dashed',
    ),
    service_colors=[
        ("#b58900", "#fdf6e3"),
        ("#2aa198", "#fdf6e3"),
        ("#268bd2", "#fdf6e3"),
        ("#dc322f", "#fdf6e3"),
        ("#859900", "#fdf6e3"),
        ("#6c71c4", "#fdf6e3"),
    ],
    group_colors=[
        ("#eee8d5", "#657b83"),
        ("#fdf6e3", "#657b83"),
        ("#b58900", "#fdf6e3"),
        ("#2aa198", "#fdf6e3"),
    ]
)
