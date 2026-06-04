from graphviz import Digraph
from typing import List, Dict, Tuple
from .node.node import Node
from .theme import Theme, DEFAULT_THEME

class FlowChart:
    # Gets a list of nodes, sort it by timestamp and returns a list of tuples [Node, Node] like
    # [(Node1, Node2), (Node2, Node3), and so on]
    @staticmethod
    def _get_edges(logs: List[Node]) -> List[tuple]:
        sorted_logs = sorted(logs, key=lambda x: x.timestamp)
        edges = []
        for i in range(len(sorted_logs) - 1):
            edges.append((sorted_logs[i], sorted_logs[i + 1]))
        return edges

    # Count the occurrences of each unique edge
    def _count_edges(self, edges: List[tuple]) -> Dict[Tuple[str, str], int]:
        edge_counts = {}
        for vert_1, vert_2 in edges:
            edge_key = (str(vert_1.getId()), str(vert_2.getId()))
            edge_counts[edge_key] = edge_counts.get(edge_key, 0) + 1
        return edge_counts

    def __init__(self, correlation_id: str, nodes: List[Node], theme: Theme = DEFAULT_THEME):
        self.correlation_id = correlation_id
        sorted_nodes = sorted(nodes, key=lambda x: x.timestamp)
        self.edges = self._get_edges(sorted_nodes)
        self.nodes = sorted_nodes
        self.start = sorted_nodes[0]
        self.end = sorted_nodes[-1]
        self.theme = theme

    def _get_subgraph_colors(self, service, color_scheme):
      index = hash(service) % len(color_scheme)  # Use hash to distribute colors
      return color_scheme[index]

    def to_graphviz(self):
        dot = Digraph(format='svg', engine='dot', graph_attr={'splines': 'ortho', 'ranksep': '0.5', 'newrank': 'true'})

        # Set the title and attributes for the graph
        dot.attr(label=f'Correlation ID: {self.correlation_id}',
                    labelloc='t', 
                    fontsize=self.theme.label.fontsize, 
                    fontname=self.theme.label.fontname,
                    bgcolor=self.theme.label.bgcolor)

        dot.attr('graph', 
                 bgcolor=self.theme.graph.bgcolor, 
                 fontcolor=self.theme.graph.fontcolor, 
                 fontname=self.theme.graph.fontname)
        
        dot.attr('node', 
                 shape=self.theme.node.shape,
                 style=self.theme.node.style,
                 fillcolor=self.theme.node.fillcolor,
                 fontcolor=self.theme.node.fontcolor,
                 fontname=self.theme.node.fontname,
                 fontsize=self.theme.node.fontsize)
        
        dot.attr('edge',
                 color=self.theme.edge.color,
                 fontcolor=self.theme.edge.color)
            
        # Add start and end nodes, pinned to top and bottom ranks
        with dot.subgraph() as s:
            s.attr(rank='min')
            s.node('S', 'start',
                   shape=self.theme.start.shape,
                   style=self.theme.start.style,
                   fillcolor=self.theme.start.fillcolor,
                   fontname=self.theme.start.fontname,
                   fontsize=self.theme.start.fontsize,
                   fontcolor=self.theme.start.fontcolor)
        with dot.subgraph() as e:
            e.attr(rank='max')
            e.node('E', 'end',
                   shape=self.theme.end.shape,
                   style=self.theme.end.style,
                   fillcolor=self.theme.end.fillcolor,
                   fontname=self.theme.end.fontname,
                   fontsize=self.theme.end.fontsize,
                   fontcolor=self.theme.end.fontcolor)
  
        # Add start connection
        dot.edge('S', str(self.start.getId()))

        for node in self.nodes:
            with dot.subgraph(name=f'cluster_{node.group}') as group:  # type: ignore
                bgcolor, line_color = self._get_subgraph_colors(node.group, self.theme.group_colors)
                group.attr(bgcolor=bgcolor, color=line_color, fontcolor=line_color)
                group.attr(label=node.group)
                with group.subgraph(name=f'cluster_{node.service}') as sub:  # type: ignore
                    bgcolor, line_color = self._get_subgraph_colors(node.service, self.theme.service_colors)
                    sub.attr(label=node.service, bgcolor=bgcolor, color=line_color, fontcolor=line_color)
                    node.addToGraph(self.theme, dot, sub)

        # Count edge occurrences and add them with labels for duplicates
        edge_counts = self._count_edges(self.edges)

        for (src_id, dest_id), count in edge_counts.items():
            if count > 1:
                # Add label showing the count and make the line bolder for repeated edges
                dot.edge(src_id, dest_id, penwidth='2', fontsize='10')
            else:
                # Single connection, regular edge
                dot.edge(src_id, dest_id)

        # Add end connection
        dot.edge(str(self.end.getId()), 'E')

        return dot

