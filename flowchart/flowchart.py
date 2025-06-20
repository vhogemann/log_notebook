import re
from graphviz import Digraph
from typing import List
from .node import Node
from .theme.theme import Theme, DEFAULT_THEME

class FlowChart:
    # Gets a list of nodes, sort it by timestamp and returns a list of tuples [Node, Node] like
    # [(Node1, Node2), (Node2, Node3), and so on]
    @staticmethod
    def _get_edges(logs: List[Node]) -> List[tuple]:
        logs.sort(key=lambda x: x.timestamp)
        edges = []
        for i in range(len(logs) - 1):
            edges.append((logs[i], logs[i + 1]))
        return edges

    def __init__(self, correlation_id: str, nodes: List[Node], theme: Theme = DEFAULT_THEME):
        self.correlation_id = correlation_id
        self.edges = self._get_edges(nodes)
        self.nodes = nodes
        self.start = nodes[0]
        self.end = nodes[-1]
        self.theme = theme

    def _get_subgraph_colors(self, service, color_scheme):
      index = hash(service) % len(color_scheme)  # Use hash to distribute colors
      return color_scheme[index]

    def to_graphviz(self):
        dot = Digraph(format='svg', engine='dot', graph_attr={'splines':'ortho'})

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

        def add_node(graph, n):
            if n.level == "ERROR":
                graph.node(str(n.id), label=n.label(), color=self.theme.error_edge.color)
                # Create a new node for the error message
                error_node_name = f"{n.className}_error"
                # Style the error node
                error_message = n.stacktrace().replace('\n', "\l")
                dot.node(error_node_name,
                          label=error_message,
                          shape=self.theme.error_note.shape, 
                          style=self.theme.error_note.style, 
                          fillcolor=self.theme.error_note.fillcolor,
                          fontname=self.theme.error_note.fontname, 
                          fontsize=self.theme.error_note.fontsize,
                          fontcolor=self.theme.error_note.fontcolor,
                          labelloc='l')  # Left-align label
                # Add an edge from the main node to the error node
                dot.edge(str(n.id), error_node_name, color=self.theme.error_edge.color, style=self.theme.error_edge.style)
            elif n.level == "WARN":
                graph.node(str(n.id), label=n.label(), color=self.theme.warn_edge.color)
                warn_node_name = f"{n.className}_warn"
                dot.node(warn_node_name,
                         label=n.stacktrace().replace('\n', "\l"),
                            shape=self.theme.warn_note.shape, 
                            style=self.theme.warn_note.style,
                            fillcolor=self.theme.warn_note.fillcolor,
                            fontname=self.theme.warn_note.fontname,
                            fontsize=self.theme.warn_note.fontsize,
                            fontcolor=self.theme.warn_note.fontcolor,
                            labelloc='l')
                dot.edge(str(n.id), warn_node_name, color=self.theme.warn_edge.color, style=self.theme.warn_edge.style)
            else:
                graph.node(str(n.id), label=n.label())
                if n.className == "WorkflowManager":
                    match = re.search(r"Workflow .* completed and went through the following checkpoints \[(.*?)\]", node.message)
                    if match:
                        steps = "\n".join(match.group(1).split(", "))
                        dot.node('workflow_steps',
                          label=steps,
                          shape=self.theme.info_note.shape, 
                          style=self.theme.info_note.style, 
                          fillcolor=self.theme.info_note.fillcolor,
                          fontname=self.theme.info_note.fontname, 
                          fontsize=self.theme.info_note.fontsize,
                          fontcolor=self.theme.info_note.fontcolor,
                          labelloc='l')
                        dot.edge(str(n.id), 'workflow_steps', color=self.theme.info_edge.color, style=self.theme.info_edge.style)
                    

        # Add start and end nodes
        dot.node('S', 'start', 
                 shape=self.theme.start.shape,
                 style=self.theme.start.style,
                 fillcolor=self.theme.start.fillcolor,
                 fontname=self.theme.start.fontname,
                 fontsize=self.theme.start.fontsize,
                 fontcolor=self.theme.start.fontcolor)
        dot.node('E', 'end', 
                 shape=self.theme.end.shape,
                 style=self.theme.end.style,
                 fillcolor=self.theme.end.fillcolor,
                 fontname=self.theme.end.fontname,
                 fontsize=self.theme.end.fontsize,
                 fontcolor=self.theme.end.fontcolor)
  
        # Add start connection
        dot.edge('S', str(self.start.id))

        add_node(dot, self.start)
        for node in self.nodes:
          with dot.subgraph(name=f'cluster_{node.group}') as group: # type: ignore
            bgcolor, line_color = self._get_subgraph_colors(node.group, self.theme.group_colors)
            group.attr(bgcolor=bgcolor, color=line_color, fontcolor=line_color)
            group.attr(label=node.group)
            with group.subgraph(name=f'cluster_{node.service}') as sub: # type: ignore
                bgcolor, line_color = self._get_subgraph_colors(node.service, self.theme.service_colors)
                sub.attr(label=node.service, bgcolor=bgcolor, color=line_color, fontcolor=line_color)
                add_node(sub, node)

        for vert_1, vert_2 in self.edges:
            dot.edge(str(vert_1.id), str(vert_2.id))

        add_node(dot, self.end)
        # Add end connection
        dot.edge(str(self.end.id), 'E')

        return dot

