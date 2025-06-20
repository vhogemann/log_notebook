# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

UNICORN_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#f8fffa',  # Minty white
        fontcolor='#7d7d7d',
        fontname='Comic Sans MS',
    ),
    label=GraphLabelStyle(
        fontname='Comic Sans MS',
        fontsize='14',
        bgcolor='#eafff5',  # Slightly minty
    ),
    edge=EdgeStyle(
        color='#b3b3b3',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#f5eaff',  # Pastel lavender
        fontname='Comic Sans MS',
        fontsize='14',
        fontcolor='#7d7d7d',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#baffc9",  # Pastel mint
        fontname='Comic Sans MS',
        fontsize='14',
        fontcolor='#7d7d7d',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#bae1ff',  # Pastel blue
        fontname='Comic Sans MS',
        fontsize='14',
        fontcolor='#7d7d7d',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffe0e9',  # Pastel pink
        fontname='Comic Sans MS',
        fontsize='10',
        fontcolor='#b47a8c',
    ),
    error_edge=EdgeStyle(
        color='#e6b3c2',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#fffacc',  # Pastel yellow
        fontname='Comic Sans MS',
        fontsize='10',
        fontcolor='#b3a86c',
    ),
    warn_edge=EdgeStyle(
        color='#e6e0b3',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#e0fff4',  # Pastel mint
        fontname='Comic Sans MS',
        fontsize='10',
        fontcolor='#7db8a3',
    ),
    info_edge=EdgeStyle(
        color='#b3e6d7',
        style='dashed',
    ),
    service_colors=[
        ("#ffe0e9", "#7d7d7d"),  # Pink
        ("#fffacc", "#7d7d7d"),  # Yellow
        ("#e0fff4", "#7d7d7d"),  # Mint
        ("#bae1ff", "#7d7d7d"),  # Blue
        ("#f5eaff", "#7d7d7d"),  # Lavender
        ("#ffd6e0", "#7d7d7d"),  # Peach
        ("#e2f0cb", "#7d7d7d"),  # Light green
        ("#f9e2ae", "#7d7d7d"),  # Light yellow
        ("#f7cac9", "#7d7d7d"),  # Blush
        ("#baffc9", "#7d7d7d"),  # Mint
        ("#c5d1eb", "#7d7d7d"),  # Light blue
        ("#f6dfeb", "#7d7d7d"),  # Light pink
    ],
    group_colors=[
        ("#f8fffa", "#b3b3b3"),
        ("#eafff5", "#b3b3b3"),
        ("#f5eaff", "#b3b3b3"),
        ("#ffe0e9", "#b3b3b3"),
        ("#fffacc", "#b3b3b3"),
        ("#e0fff4", "#b3b3b3"),
        ("#bae1ff", "#b3b3b3"),
        ("#ffd6e0", "#b3b3b3"),
    ]
)