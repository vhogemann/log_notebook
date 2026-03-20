from dataclasses import dataclass
from typing import List, Tuple

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
        ("#b3d1ff", "#345678"),  # Muted blue
        ("#cce6ff", "#3a5068"),  # Muted blue-gray
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
        ("#a3c1ad", "#222222"),  # Muted teal
        ("#2980b9", "#ffffff"),
        ("#16a085", "#ffffff"), 
        ("#6c7a89", "#ffffff"),  # Muted blue-gray
    ],
    group_colors=[
        ("#3a3a3a", "#cccccc"),
        ("#2c3e50", "#ffffff"),
        ("#1a252f", "#ffffff"),
        ("#2e4057", "#ffffff"),
    ],
)


def make_theme(
    fontname: str,
    graph_bgcolor: str,
    graph_fontcolor: str,
    label_bgcolor: str,
    edge_color: str,
    node_fillcolor: str,
    node_fontcolor: str,
    start_fillcolor: str,
    start_fontcolor: str,
    end_fillcolor: str,
    end_fontcolor: str,
    error_fillcolor: str,
    error_fontcolor: str,
    error_edge_color: str,
    warn_fillcolor: str,
    warn_fontcolor: str,
    warn_edge_color: str,
    info_fillcolor: str,
    info_fontcolor: str,
    info_edge_color: str,
    service_colors: List[Tuple[str, str]],
    group_colors: List[Tuple[str, str]],
    note_fontsize: str = '10',
) -> Theme:
    return Theme(
        graph=GraphStyle(bgcolor=graph_bgcolor, fontcolor=graph_fontcolor, fontname=fontname),
        label=GraphLabelStyle(fontname=fontname, fontsize='14', bgcolor=label_bgcolor),
        edge=EdgeStyle(color=edge_color, style=''),
        node=NodeStyle(shape='box', style='rounded,filled', fillcolor=node_fillcolor, fontname=fontname, fontsize='14', fontcolor=node_fontcolor),
        start=NodeStyle(shape='circle', style='filled', fillcolor=start_fillcolor, fontname=fontname, fontsize='14', fontcolor=start_fontcolor),
        end=NodeStyle(shape='doublecircle', style='filled', fillcolor=end_fillcolor, fontname=fontname, fontsize='14', fontcolor=end_fontcolor),
        error_note=NodeStyle(shape='note', style='filled', fillcolor=error_fillcolor, fontname=fontname, fontsize=note_fontsize, fontcolor=error_fontcolor),
        error_edge=EdgeStyle(color=error_edge_color, style='dashed'),
        warn_note=NodeStyle(shape='note', style='filled', fillcolor=warn_fillcolor, fontname=fontname, fontsize=note_fontsize, fontcolor=warn_fontcolor),
        warn_edge=EdgeStyle(color=warn_edge_color, style='dashed'),
        info_note=NodeStyle(shape='note', style='filled', fillcolor=info_fillcolor, fontname=fontname, fontsize='10', fontcolor=info_fontcolor),
        info_edge=EdgeStyle(color=info_edge_color, style='dashed'),
        service_colors=service_colors,
        group_colors=group_colors,
    )