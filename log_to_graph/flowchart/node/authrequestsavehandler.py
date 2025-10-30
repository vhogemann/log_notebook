from graphviz import Digraph
from .dtopp import dto_pp
from .node import Node
from ..theme.theme import Theme


class AuthRequestSaveHandler(Node):
    def addNote(self, theme: Theme, graph: Digraph):
        pass
        # message = dto_pp(self.message)
        # graph.node(f'{self.getId()}_message',
        #             label=message,
        #             shape=theme.info_note.shape, 
        #             style=theme.info_note.style,
        #             fillcolor=theme.info_note.fillcolor,
        #             fontname=theme.info_note.fontname, 
        #             fontsize=theme.info_note.fontsize,
        #             fontcolor=theme.info_note.fontcolor,
        #             labelloc='l')
        # graph.edge(str(self.getId()), f'{self.getId()}_message', color=theme.info_edge.color, style=theme.info_edge.style)