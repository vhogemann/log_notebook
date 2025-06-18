import re
import uuid
from graphviz import Digraph
from typing import List
from datetime import datetime
from dateutil.relativedelta import relativedelta
import humanize

def format_stacktrace(message: str) -> str:
    stacktrace = []
    for line in message.split("\n"):
        if line.strip().startswith("at "):
            if "com.starlingbank" in line:
                stacktrace.append(line)
            elif len(stacktrace) > 0 and stacktrace[-1] != "...":
                stacktrace.append("...")
        else:
            stacktrace.append(line)
    return "\n".join(stacktrace)

class Node:
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
      return format_stacktrace(self.message)

    def _package_name(self, class_name):
        if "." in class_name:
            components = class_name.split(".")
            package = ".".join(components[:-1])
            return package
        else:
          return ""

    def __init__(self, event):
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

    def label(self):
        return f"""<
        <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
        <TR><TD ALIGN="CENTER"><FONT POINT-SIZE="8">{self.packageName}</FONT></TD></TR>
        <TR><TD ALIGN="CENTER"><FONT POINT-SIZE="10">{self.className}</FONT></TD></TR>
        </TABLE>
        >"""

    def __str__(self):
        return f"{self.className}"

class FlowChart:
    # Gets a list of nodes, sort it by timestamp and returns a list of tuples [Node, Node] like
    # [(Node1, Node2), (Node2, Node3), and so on]
    @staticmethod
    def _get_edges(logs: List[Node]) -> List[tuple]:
        logs.sort(key=lambda x: x.timestamp)
        edges = []
        for i in range(len(logs) - 1):
            edges.append((logs[i], logs[i + 1]))
        return edges

    def __init__(self, correlation_id: str, nodes: List[Node]):
        self.correlation_id = correlation_id
        self.edges = self._get_edges(nodes)
        self.nodes = nodes
        self.start = nodes[0]
        self.end = nodes[-1]

    @staticmethod
    def _get_subgraph_colors(service):
      colors = [
        ("#4a6572", "#9fb3bc"),  # Steel Teal, Cadet Blue
        ("#528b81", "#7cb9b4"),  # Sea Green, Aquamarine
        ("#8064a2", "#9e81ba"),  # Slate Purple, Medium Purple
        ("#b4865a", "#c9a27b"),  # Peru Brown, Sandy Brown
        ("#a54e4e", "#b97373"),  # Indian Red, Rosy Brown
        ("#4e78a5", "#7397c0"),  # Steel Blue, Light Steel Blue
        ("#5fa25f", "#85ba85"),  # Dark Sea Green, Pale Green
        ("#8b6f4e", "#a68d73"),  # Sienna Brown, Tan
        ("#7f8c8d", "#95a5a6"),  # Gray, Light Gray
        ("#85929e", "#aeb6bf"),  # Blue Gray, Light Blue Gray
        ("#2c3e50", "#34495e"),  # Midnight Blue, Dark Blue
        ("#186a3b", "#27ae60"),  # Dark Green, Emerald Green
        ("#9b59b6", "#8e44ad"),  # Purple, Darker Purple
        ("#f39c12", "#e67e22"),  # Orange, Darker Orange
        ("#2980b9", "#3498db"),  # Blue, Darker Blue
        ("#16a085", "#1abc9c"),  # Turquoise, Darker Turquoise
        ("#d35400", "#e67e22"),  # Orange, Darker Orange
        ("#ba4a00", "#d35400"),  # Dark Orange, Orange
      ]
      index = hash(service) % len(colors)  # Use hash to distribute colors
      return colors[index]

    def to_graphviz(self):
        dot = Digraph(format='svg', engine='dot', graph_attr={'splines':'ortho'})

        # Set the title and attributes for the graph
        dot.attr(label=f'Correlation ID: {self.correlation_id}',
                    labelloc='t', 
                    fontsize='14', 
                    fontname='sans-serif',
                    bgcolor='#f0f0f0')

        # Set dark mode styles
        dot.attr('graph', bgcolor='#2e2e2e', fontcolor='white', fontname='sans-serif')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='#4e4e4e', fontcolor='white', fontname='sans-serif')
        dot.attr('edge', color='white', fontcolor='white', fontname='sans-serif')

        def add_node(graph, n):
            if n.level == "ERROR":
                graph.node(str(n.id), label=n.label(), style='rounded,filled', color='red', fillcolor='#4e4e4e')
                # Create a new node for the error message
                error_node_name = f"{n.className}_error"
                # Style the error node
                error_message = n.stacktrace().replace('\n', "\l")
                dot.node(error_node_name,
                          label=error_message,
                          shape='note', style='filled', fillcolor='#ffcccc',
                          fontname='sans-serif', fontsize='8',
                          fontcolor='#800020',
                          labelloc='l')  # Left-align label
                # Add an edge from the main node to the error node
                dot.edge(str(n.id), error_node_name, color='red', style='dashed')
            elif n.level == "WARN":
                graph.node(str(n.id), label=n.label(), style='rounded,filled', color='orange', fillcolor='#4e4e4e')
                warn_node_name = f"{n.className}_warn"
                dot.node(warn_node_name,
                         label=n.stacktrace().replace('\n', "\l"),
                            shape='note', style='filled', fillcolor='#ffebcc',
                            fontname='sans-serif', fontsize='8',
                            fontcolor='#805000',
                            labelloc='l')
                dot.edge(str(n.id), warn_node_name, color='orange', style='dashed')
            else:
                graph.node(str(n.id), label=n.label())
                if n.className == "WorkflowManager":
                    match = re.search(r"Workflow .* completed and went through the following checkpoints \[(.*?)\]", node.message)
                    if match:
                        steps = "\n".join(match.group(1).split(", "))
                        dot.node('workflow_steps',
                          label=steps,
                          shape='note', style='filled', fillcolor="#d6fdac",
                          fontname='sans-serif', fontsize='8',
                          fontcolor="#008000",
                          labelloc='l')
                        dot.edge(str(n.id), 'workflow_steps', color='green', style='dashed')
                    

        # Add start and end nodes
        dot.node('S', 'start', shape='circle')
        dot.node('E', 'end', shape='circle')

        # Add start connection
        dot.edge('S', str(self.start.id))

        add_node(dot, self.start)
        for node in self.nodes:
          with dot.subgraph(name=f'cluster_{node.group}') as group:
            group.attr(label=node.group)
            with group.subgraph(name=f'cluster_{node.service}') as sub:
                bgcolor, line_color = self._get_subgraph_colors(node.service)
                sub.attr(label=node.service, bgcolor=bgcolor, color=line_color)
                add_node(sub, node)

        for vert_1, vert_2 in self.edges:
            dot.edge(str(vert_1.id), str(vert_2.id))

        add_node(dot, self.end)
        # Add end connection
        dot.edge(str(self.end.id), 'E')

        return dot

