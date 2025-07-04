# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

HOTDOG_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#ffffff',  # White background
        fontcolor='#000000',  # Black text
        fontname='Courier New',
    ),
    label=GraphLabelStyle(
        fontname='Courier New',
        fontsize='14',
        bgcolor='#ff0000',  # Red
    ),
    edge=EdgeStyle(
        color='#000000',  # Black for max contrast
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#ffcc00',  # Bright yellow
        fontname='Courier New',
        fontsize='14',
        fontcolor='#000000',  # Black text
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#ff0000",  # Red
        fontname='Courier New',
        fontsize='14',
        fontcolor='#ffffff',  # White text
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#000000',  # Black
        fontname='Courier New',
        fontsize='14',
        fontcolor='#ffcc00',  # Yellow text
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ff0000',  # Red
        fontname='Courier New',
        fontsize='10',
        fontcolor='#ffffff',  # White text
    ),
    error_edge=EdgeStyle(
        color='#ff0000',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffcc00',  # Yellow
        fontname='Courier New',
        fontsize='10',
        fontcolor='#000000',  # Black text
    ),
    warn_edge=EdgeStyle(
        color='#ffcc00',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffffff',  # White
        fontname='Courier New',
        fontsize='10',
        fontcolor='#000000',  # Black text
    ),
    info_edge=EdgeStyle(
        color='#000000',
        style='dashed',
    ),
    service_colors=[
        ("#ffcc00", "#000000"),  # Yellow bg, black text
        ("#ff0000", "#ffffff"),  # Red bg, white text
        ("#000000", "#ffcc00"),  # Black bg, yellow text
        ("#ffffff", "#ff0000"),  # White bg, red text
        ("#000000", "#ffffff"),  # Black bg, white text
        ("#ffffff", "#000000"),  # White bg, black text
        ("#ffcc00", "#ff0000"),  # Yellow bg, red text
        ("#ff0000", "#ffcc00"),  # Red bg, yellow text
    ],
    group_colors=[
        ("#ffffff", "#000000"),  # White bg, black text
        ("#ffcc00", "#000000"),  # Yellow bg, black text
        ("#ff0000", "#ffffff"),  # Red bg, white text
        ("#000000", "#ffcc00"),  # Black bg, yellow text
        ("#ffcc00", "#ff0000"),  # Yellow bg, red text
        ("#ff0000", "#ffcc00"),  # Red bg, yellow text
        ("#000000", "#ffffff"),  # Black bg, white text
        ("#ffffff", "#ff0000"),  # White bg, red text
    ]
)
