from .node import Node

def node_factory(event:dict) -> Node:
    return Node(event)