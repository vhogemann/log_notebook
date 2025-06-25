import re
from ..node.node import Node
from .message_parser import IMessageParser
from typing import Union

class WorkflowMessageParser(IMessageParser):
    """
    Parser for workflow messages.
    This parser will extract the workflow information from the node and format it.
    """

    def parse(self, node: Node) -> Union[str, None]:
        """
        Parse the workflow information from the node.
        """
        match = re.search(r"Workflow .* completed and went through the following checkpoints \[(.*?)\]", node.message)
        if match :
            return "\n".join(match.group(1).split(", "))
        else:
            return None
        

    def match(self, node: Node) -> bool:
        """
        Check if the node is a workflow message.
        """
        return node.className == "WorkflowManager"