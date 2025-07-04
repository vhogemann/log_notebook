import re
from typing import Optional
# DTO Pretty Printer
# Util method to extrat the string representation of a DTO from a log message
# and format it for better readability


def __extract_dto_from_log(message: str) -> Optional[str]:
    match = re.search(r'(\w*{.*})', message)
    if match:
        extracted_message = match.group(1)
        return __format_message(extracted_message)
    return None

def __format_message(message: str) -> Optional[str]:
    def format_message_inner(message: str, tabsize, acc) -> str:
        if message.__len__() == 0:
            return acc
        head, *tail = message
        if head == '{':
            acc += head + '\l' + ' ' * (tabsize + 4) 
            return format_message_inner(''.join(tail), tabsize + 4, acc)
        elif head == '}':
            acc += '\l' + ' ' * (tabsize - 4) + head
            return format_message_inner(''.join(tail), tabsize - 4, acc)
        elif head == ',':
            acc += head + '\l' + ' ' * tabsize
            return format_message_inner(''.join(tail), tabsize, acc)
        elif head == ' ':
            return format_message_inner(''.join(tail), tabsize, acc)
        else:
            acc += head
            return format_message_inner(''.join(tail), tabsize, acc)
    return format_message_inner(message, 0, '')

def dto_pp(message: str) -> Optional[str]:
    """
    Pretty prints a DTO from a log message.
    
    Args:
        message (str): The log message containing the DTO.
        
    Returns:
        str: The pretty printed DTO string.
    """
    dto = __extract_dto_from_log(message)
    if dto:
        return __format_message(dto)
    return None