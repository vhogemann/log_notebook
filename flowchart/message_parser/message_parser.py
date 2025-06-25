from abc import ABC, abstractmethod
from typing import Union

from flowchart.node.node import Node

class IMessageParser(ABC):
    """
    Interface for message parsers.
    These will check if they can handle a node and parse it accordingly.
    """

    @abstractmethod
    def parse(self, node:Node) -> Union[str, None]:
        """
        Parse the node message, extrancting relevant information, and applying any necessary transformations.
        """
        pass


    @abstractmethod
    def match(self, node: Node) -> bool:
        """
        Check if the parser can handle the given node.
        """
        return False