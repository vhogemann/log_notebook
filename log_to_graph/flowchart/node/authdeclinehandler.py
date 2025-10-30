import re
from graphviz import Digraph
from .node import Node
from ..theme.theme import Theme
# Auth request declined for Message: MC-20250904-MDHLO8D2J, response code: Code 05 "Do not honor" , decline reason: TRACK_DATA_INVALID
class AuthDeclineHandler(Node):
    def addNote(self, theme: Theme, graph: Digraph):
        match = re.search(r'Auth request declined for Message: ([\w-]+), response code: Code (\d+) \"([^"]+)\"', self.message)
        if match :
            message_id = match.group(1)
            response_code = match.group(2)
            response_reason = match.group(3)
            formatted_message = f"Message ID: {message_id}\nResponse Code: {response_code}\nReason: {response_reason}"
            graph.node(f'{self.getId()}_message',
                        label=formatted_message,
                        shape=theme.info_note.shape, 
                        style=theme.info_note.style,
                        fillcolor=theme.info_note.fillcolor,
                        fontname=theme.info_note.fontname, 
                        fontsize=theme.info_note.fontsize,
                        fontcolor=theme.info_note.fontcolor,
                        labelloc='l')
            graph.edge(str(self.getId()), f'{self.getId()}_message', color=theme.info_edge.color, style=theme.info_edge.style)
