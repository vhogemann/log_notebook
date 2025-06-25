import uuid
from datetime import datetime
from graphviz import Digraph
import humanize

from flowchart.theme.theme import Theme

class Node:

    def __init__(self, event:dict):
        self.id = str(uuid.uuid4())
        if "class" in event:
            self.className = self._class_name(event["class"])
            self.packageName = self._package_name(event["class"])
        else:
            self.className = "Unknown"
            self.packageName = "unknown"

        if "level" in event:
            self.level = event["level"]
        else:
            self.level = "INFO"

        self.timestamp = event["@timestamp"]
        self.relative_time = self._format_timestamp(self.timestamp)
        self.message = event["message"]
        self.service = event["service"]
        self.group = event["engineering_group"].lower()
        self.correlation_id = event["correlation_id"]


    # Takes a Java class name and returns the class name without the package name
    @staticmethod
    def _class_name(class_name):
        if "." in class_name:
            components = class_name.split(".")
            class_name = f"{components[- 1]}"
        return class_name

    # Takes the timestamp and formats it to a human-readable format
    @staticmethod
    def _format_timestamp(timestamp):
        # Convert the timestamp to a datetime object
        dt = datetime.fromtimestamp(timestamp / 1000.0)
        # Get the current time
        now = datetime.now()
        # Format the difference in a human-readable way
        return f"{humanize.precisedelta(now - dt)} ago"

    def stacktrace(self):
        stacktrace = []
        for line in self.message.split("\n"):
            if line.strip().startswith("at "):
                if "com.starlingbank" in line:
                    stacktrace.append(line)
                elif len(stacktrace) > 0 and stacktrace[-1] != "...":
                    stacktrace.append("...")
            else:
                stacktrace.append(line)
        return "\n".join(stacktrace)

    def _package_name(self, class_name):
        if "." in class_name:
            components = class_name.split(".")
            package = ".".join(components[:-1])
            return package
        else:
          return ""

    def label(self):
        return f"""<
        <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
        <TR><TD ALIGN="CENTER"><FONT POINT-SIZE="8">{self.packageName}</FONT></TD></TR>
        <TR><TD ALIGN="CENTER"><FONT POINT-SIZE="10">{self.className}</FONT></TD></TR>
        </TABLE>
        >"""

    def __str__(self):
        return f"{self.className}"
    
    def _linecolor(self, theme:Theme):
        if self.level == "ERROR":
            return theme.error_edge.color
        elif self.level == "WARN":
            return theme.warn_edge.color
        elif self.level == "INFO":
            return theme.info_edge.color
        else:
            return theme.edge.color

    def addToGraph(self, theme: Theme, graph:Digraph):
        graph.node(str(self.id), 
                    label=self.label(), 
                    shape=theme.node.shape, 
                    style=theme.node.style, 
                    color=self._linecolor(theme),
                    fillcolor=theme.node.fillcolor, 
                    fontname=theme.node.fontname, 
                    fontsize=theme.node.fontsize, 
                    fontcolor=theme.node.fontcolor)
        return graph
