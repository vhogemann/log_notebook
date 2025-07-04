# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

GAMEBOY_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#9bbc0f',
        fontcolor='#0f380f',
        fontname='Courier New',
    ),
    label=GraphLabelStyle(
        fontname='Courier New',
        fontsize='14',
        bgcolor='#8bac0f',
    ),
    edge=EdgeStyle(
        color='#306230',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#8bac0f',
        fontname='Courier New',
        fontsize='14',
        fontcolor='#0f380f',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#306230",
        fontname='Courier New',
        fontsize='14',
        fontcolor='#e0f8d0',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#0f380f',
        fontname='Courier New',
        fontsize='14',
        fontcolor='#e0f8d0',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#e0f8d0',
        fontname='Courier New',
        fontsize='10',
        fontcolor='#0f380f',
    ),
    error_edge=EdgeStyle(
        color='#e0f8d0',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#8bac0f',
        fontname='Courier New',
        fontsize='10',
        fontcolor='#0f380f',
    ),
    warn_edge=EdgeStyle(
        color='#8bac0f',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#9bbc0f',
        fontname='Courier New',
        fontsize='10',
        fontcolor='#0f380f',
    ),
    info_edge=EdgeStyle(
        color='#9bbc0f',
        style='dashed',
    ),
    service_colors=[
        ("#8bac0f", "#0f380f"),
        ("#306230", "#e0f8d0"),
        ("#0f380f", "#e0f8d0"),
        ("#e0f8d0", "#0f380f"),
    ],
    group_colors=[
        ("#9bbc0f", "#0f380f"),
        ("#8bac0f", "#0f380f"),
        ("#306230", "#e0f8d0"),
        ("#0f380f", "#e0f8d0"),
    ]
)
