# This file was moved to the theme/ subpackage.

from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class GraphStyle:
    bgcolor: str
    fontcolor: str
    fontname: str

@dataclass(frozen=True)
class GraphLabelStyle:
    fontname: str
    fontsize: str
    bgcolor: str

@dataclass(frozen=True)
class NodeStyle:
    shape: str  # Node shape
    style: str  # Node style
    fillcolor: str  # Node fill color
    fontname: str  # Font name for the node label
    fontsize: str  # Font size for the node label
    fontcolor: str  # Font color for the node label

@dataclass(frozen=True)
class EdgeStyle:
    color: str
    style: str

@dataclass(frozen=True)
class Theme:
    graph: GraphStyle  # Graph style
    label: GraphLabelStyle
    edge: EdgeStyle
    node: NodeStyle  # Default node style
    start: NodeStyle  # Style for START nodes
    end: NodeStyle # Style for END nodes
    error_note: NodeStyle # Style for ERROR notes
    error_edge: EdgeStyle  # Style for edges leading to ERROR notes
    warn_note: NodeStyle  # Style for WARN notes
    warn_edge: EdgeStyle # Style for edges leading to WARN notes
    info_note: NodeStyle   # Style for INFO notes
    info_edge: EdgeStyle # Style for edges leading to INFO notes
    service_colors: list[Tuple[str, str]]  # List of (foreground, background) color pairs for service subgraphs
    group_colors: list[Tuple[str, str]]  # Optional group colors for subgraphs

# Default theme for the flowchart
DEFAULT_THEME = Theme(
    graph=GraphStyle(
        bgcolor='#2e2e2e',
        fontcolor='#ffffff',
        fontname='Arial',
    ),
    label=GraphLabelStyle(
        fontname='Arial',
        fontsize='14',
        bgcolor='#222222',
    ),
    edge=EdgeStyle(
        color='#cccccc',
        style='',  # No explicit style for default edges
    ),
    node=NodeStyle(
        shape='box',
        style='rounded,filled',
        fillcolor='#4e4e4e',
        fontname='Arial',
        fontsize='14',
        fontcolor='#ffffff',
    ),
    start=NodeStyle(
        shape='circle',
        style='filled',
        fillcolor="#97c253",
        fontname='Arial',
        fontsize='14',
        fontcolor='#222222',
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
        fillcolor='#ffebcc',
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
        fillcolor='#d6fdac',
        fontname='Arial',
        fontsize='10',
        fontcolor='#006400',
    ),
    info_edge=EdgeStyle(
        color='#006400',
        style='dashed',
    ),
    service_colors=[
        ("#ffffff", "#4e4e4e"), 
        ("#ffcccc", "#800020"), 
        ("#ffebcc", "#805000"),
        ("#d6fdac", "#006400"), 
        ("#b4865a", "#222222"), 
        ("#4e78a5", "#ffffff"),
        ("#5fa25f", "#222222"), 
        ("#8b6f4e", "#ffffff"), 
        ("#7f8c8d", "#ffffff"),
        ("#85929e", "#ffffff"), 
        ("#2c3e50", "#ffffff"), 
        ("#186a3b", "#ffffff"),
        ("#9b59b6", "#ffffff"), 
        ("#f39c12", "#222222"), 
        ("#2980b9", "#ffffff"),
        ("#16a085", "#ffffff"), 
        ("#d35400", "#ffffff"), 
        ("#ba4a00", "#ffffff"),
    ],
    group_colors=[
        ("#bbbbbb", "#383838"),
        ("#888888", "#323232"),
        ("#666666", "#2a2a2a"),
        ("#444444", "#242424"),
        ("#999999", "#303030"),
        ("#aaaaaa", "#353535"),
        ("#777777", "#292929"),
        ("#555555", "#202020"),
    ]
)