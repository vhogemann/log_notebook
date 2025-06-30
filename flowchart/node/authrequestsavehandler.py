from graphviz import Digraph
from flowchart.theme.theme import Theme


class AuthRequestSaveHandler(Node):
    """
    Node to handle the saving of an authentication request.
    """

    def __init__(self, message: str):
        super().__init__(message)

    def addNote(self, theme: Theme, graph: Digraph):
        graph.node(self.id, label=self.message, shape='box', style='filled', fillcolor=theme.auth_request_save_node.fillcolor,
                   fontcolor=theme.auth_request_save_node.fontcolor, fontsize=theme.auth_request_save_node.fontsize)
        graph.edge(self.id, self.get_next_id(), color=self.get_edge_color(theme))