# This file was moved to the theme/ subpackage.

from .theme import Theme, GraphStyle, GraphLabelStyle, EdgeStyle, NodeStyle

# A light theme for the flowchart
LIGHT_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#ffffff',
        fontcolor='#222222',
        fontname='Arial',
    ),
    label=GraphLabelStyle(
        fontname='Arial',
        fontsize='14',
        bgcolor='#f5f5f5',
    ),
    edge=EdgeStyle(
        color='#444444',
        style='',  # No explicit style for default edges
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#e0e0e0',
        fontname='Arial',
        fontsize='14',
        fontcolor='#222222',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#97c253",
        fontname='Arial',
        fontsize='14',
        fontcolor='#ffffff',
    ),
    end=NodeStyle(
        shape='doublecircle',
        style='filled',
        fillcolor='#4e78a5',
        fontname='Arial',
        fontsize='14',
        fontcolor='#ffffff',
    ),
    error_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#ffcccc',
        fontname='Arial',
        fontsize='8',
        fontcolor='#800020',
    ),
    error_edge=EdgeStyle(
        color='#b00020',
        style='dashed',
    ),
    warn_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#fff4cc',
        fontname='Arial',
        fontsize='8',
        fontcolor='#805000',
    ),
    warn_edge=EdgeStyle(
        color='#b8860b',
        style='dashed',
    ),
    info_note=NodeStyle(
        shape='note',
        style='filled',
        fillcolor='#e6ffd6',
        fontname='Arial',
        fontsize='10',
        fontcolor='#006400',
    ),
    info_edge=EdgeStyle(
        color='#006400',
        style='dashed',
    ),
    service_colors=[
        ("#ffb3ba", "#6d214f"),   # Pastel pink bg, deep magenta text
        ("#ffdfba", "#6d4c1b"),   # Pastel orange bg, brown text
        ("#ffffba", "#7a7a00"),   # Pastel yellow bg, olive text
        ("#baffc9", "#006d5b"),   # Pastel green bg, teal text
        ("#bae1ff", "#1b4c6d"),   # Pastel blue bg, navy text
        ("#e2baff", "#4c1b6d"),   # Pastel purple bg, purple text
        ("#bafff7", "#006d6d"),   # Pastel mint bg, teal text
        ("#ffd6fa", "#6d1b5e"),   # Pastel lavender bg, magenta text
        ("#fff0ba", "#7a6d00"),   # Pastel cream bg, dark gold text
        ("#c9baff", "#2d1b6d"),   # Pastel violet bg, indigo text
        ("#bae7ff", "#1b3a6d"),   # Pastel sky bg, blue text
        ("#ffbad6", "#6d1b3a"),   # Pastel rose bg, burgundy text
        ("#d6ffba", "#3a6d1b"),   # Pastel lime bg, green text
        ("#f7baff", "#6d1b4c"),   # Pastel pink-violet bg, magenta text
        ("#baffd6", "#1b6d4c"),   # Pastel aqua bg, teal text
        ("#faffba", "#6d6d1b"),   # Pastel lemon bg, olive text
        ("#babaff", "#1b1b6d"),   # Pastel indigo bg, navy text
        ("#ffbab3", "#6d2d1b"),   # Pastel coral bg, brown text
    ],
    group_colors=[
        ("#ffe4ec", "#6d214f"),   # Pastel pink bg, deep magenta text
        ("#fff5e1", "#6d4c1b"),   # Pastel orange bg, brown text
        ("#f9ffe1", "#7a7a00"),   # Pastel yellow bg, olive text
        ("#e1fff0", "#006d5b"),   # Pastel green bg, teal text
        ("#e1f0ff", "#1b4c6d"),   # Pastel blue bg, navy text
        ("#f0e1ff", "#4c1b6d"),   # Pastel purple bg, purple text
        ("#e1fff9", "#006d6d"),   # Pastel mint bg, teal text
        ("#ffe1f9", "#6d1b5e"),   # Pastel lavender bg, magenta text
    ]
)