from .authdeclinehandler import AuthDeclineHandler
from .authrequestsavehandler import AuthRequestSaveHandler
from .node import Node
from .workflow import WorkflowManagerNode

def node_factory(event:dict) -> Node:
    if(event.get('class') is None):
        return Node(event)
    if(event['class'] == 'com.starlingbank.workflow.WorkflowManager'):
        return WorkflowManagerNode(event)
    elif(event['class'] == 'com.starlingbank.cardprocessor.workflow.auth.handlers.AuthRequestSaveHandler'):
        return AuthRequestSaveHandler(event)
    elif(event['class'] == 'com.starlingbank.cardprocessor.workflow.auth.handlers.AuthDeclineHandler'):
        return AuthDeclineHandler(event)
    else:
        return Node(event)