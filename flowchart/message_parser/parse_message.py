    
from flowchart.message_parser.stacktrace import StackTraceMessageParser
from flowchart.message_parser.workflow import WorkflowMessageParser
from flowchart.node.node import Node


__PARSERS = [
    StackTraceMessageParser(),
    WorkflowMessageParser()
]

def parse_message(node: Node) -> list[str]:
    """
    Parse the message of a node using the appropriate parsers.
    """
    messages = []
    for parser in __PARSERS:
        if parser.match(node):
            parsed_message = parser.parse(node)
            if parsed_message:
                messages.append(parsed_message)
    return messages