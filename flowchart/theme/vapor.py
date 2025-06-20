# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

VAPORWAVE_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#2d0036',  # Deep purple
        fontcolor='#f8f8f2',
        fontname='Monaco',
    ),
    label=GraphLabelStyle(
        fontname='Monaco',
        fontsize='14',
        bgcolor='#ff71ce',  # Neon pink
    ),
    edge=EdgeStyle(
        color='#05ffa1',  # Neon green
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#01cdfe',  # Neon blue
        fontname='Monaco',
        fontsize='14',
        fontcolor='#f8f8f2',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#ff71ce",  # Neon pink
        fontname='Monaco',
        fontsize='14',
        fontcolor='#2d0036',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#05ffa1',  # Neon green
        fontname='Monaco',
        fontsize='14',
        fontcolor='#2d0036',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ff206e',  # Hot pink
        fontname='Monaco',
        fontsize='10',
        fontcolor='#f8f8f2',
    ),
    error_edge=EdgeStyle(
        color='#ff206e',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#fbff12',  # Neon yellow
        fontname='Monaco',
        fontsize='10',
        fontcolor='#2d0036',
    ),
    warn_edge=EdgeStyle(
        color='#fbff12',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#01cdfe',  # Neon blue
        fontname='Monaco',
        fontsize='10',
        fontcolor='#2d0036',
    ),
    info_edge=EdgeStyle(
        color='#01cdfe',
        style='dashed',
    ),
    service_colors=[
        ("#ff71ce", "#2d0036"),  # Neon pink
        ("#01cdfe", "#2d0036"),  # Neon blue
        ("#05ffa1", "#2d0036"),  # Neon green
        ("#fbff12", "#2d0036"),  # Neon yellow
        ("#b967ff", "#2d0036"),  # Neon purple
        ("#ff206e", "#f8f8f2"),  # Hot pink
        ("#f8f8f2", "#2d0036"),  # White
        ("#2d0036", "#ff71ce"),  # Inverted
    ],
    group_colors=[
        ("#2d0036", "#ff71ce"),
        ("#2d0036", "#01cdfe"),
        ("#2d0036", "#05ffa1"),
        ("#2d0036", "#fbff12"),
        ("#2d0036", "#b967ff"),
        ("#2d0036", "#ff206e"),
        ("#2d0036", "#f8f8f2"),
        ("#ff71ce", "#2d0036"),
    ]
)
