from typing import Union
from ..node.node import Node
from .message_parser import IMessageParser

class StackTraceMessageParser(IMessageParser):
    """
    Parser for stack trace messages.
    This parser will extract the stack trace from the node and format it.
    """
    
    def parse(self, node: Node) -> Union[str, None]:
        """
        Parse the stack trace from the node.
        """
        stacktrace = []
        for line in node.message.split("\n"):
            if line.strip().startswith("at "):
                if "com.starlingbank" in line:
                    stacktrace.append(line)
                elif len(stacktrace) > 0 and stacktrace[-1] != "...":
                    stacktrace.append("...")
            else:
                stacktrace.append(line)
        return "\n".join(stacktrace)

    def match(self, node: Node) -> bool:
        """
        Check if the node has a stack trace.
        """
        return node.level == "ERROR"