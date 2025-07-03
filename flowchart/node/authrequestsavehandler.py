from graphviz import Digraph
from flowchart.node.dtopp import dto_pp
from flowchart.node.node import Node
from flowchart.theme.theme import Theme

class AuthRequestSaveHandler(Node):
    def addNote(self, theme: Theme, graph: Digraph):
        message = dto_pp(self.message)
        print(f"Adding AuthRequestSaveHandler note with message: {message}")
        graph.node(f'{self.id}_message',
                    label=message,
                    shape=theme.info_note.shape, 
                style=theme.info_note.style, 
                    fillcolor=theme.info_note.fillcolor,
                    fontname=theme.info_note.fontname, 
                    fontsize=theme.info_note.fontsize,
                    fontcolor=theme.info_note.fontcolor,
                    labelloc='l')
        graph.edge(str(self.id), f'{self.id}_message', color=theme.info_edge.color, style=theme.info_edge.style)