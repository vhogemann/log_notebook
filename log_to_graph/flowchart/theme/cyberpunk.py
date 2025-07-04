# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

CYBERPUNK_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#18181a',
        fontcolor='#ff00c8',
        fontname='Arial',  # Changed from Orbitron to Arial for better compatibility
    ),
    label=GraphLabelStyle(
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='14',
        bgcolor='#00fff7',
    ),
    edge=EdgeStyle(
        color='#ffea00',
        style='',
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#ff00c8',
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='14',
        fontcolor='#18181a',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#00fff7",
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='14',
        fontcolor='#18181a',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#ffea00',
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='14',
        fontcolor='#18181a',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ff003c',
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='10',
        fontcolor='#00fff7',
    ),
    error_edge=EdgeStyle(
        color='#ff003c',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffea00',
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='10',
        fontcolor='#18181a',
    ),
    warn_edge=EdgeStyle(
        color='#ffea00',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#00fff7',
        fontname='Arial',  # Changed from Orbitron to Arial
        fontsize='10',
        fontcolor='#18181a',
    ),
    info_edge=EdgeStyle(
        color='#00fff7',
        style='dashed',
    ),
    service_colors=[
        ("#ff00c8", "#18181a"),
        ("#00fff7", "#18181a"),
        ("#ffea00", "#18181a"),
        ("#ff003c", "#00fff7"),
        ("#18181a", "#ff00c8"),
    ],
    group_colors=[
        ("#18181a", "#ff00c8"),
        ("#00fff7", "#18181a"),
        ("#ffea00", "#18181a"),
        ("#ff00c8", "#18181a"),
    ]
)
