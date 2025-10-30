import re
from graphviz import Digraph
from ..theme.theme import Theme
from .node import Node

class WorkflowManagerNode(Node):
    def addNote(self, theme: Theme, graph: Digraph):
        match = re.search(r"Workflow .* completed and went through the following checkpoints \[(.*?)\]", self.message)
        if match :
            steps = "\n".join(match.group(1).split(", "))
            graph.node(f'{self.getId()}_workflow_steps',
                        label=steps,
                        shape=theme.info_note.shape, 
                        style=theme.info_note.style, 
                        fillcolor=theme.info_note.fillcolor,
                        fontname=theme.info_note.fontname, 
                        fontsize=theme.info_note.fontsize,
                        fontcolor=theme.info_note.fontcolor,
                        labelloc='l')
            graph.edge(str(self.getId()), f'{self.getId()}_workflow_steps', color=theme.info_edge.color, style=theme.info_edge.style)