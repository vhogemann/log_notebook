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
    acc = ''
    tabsize = 0
    for char in message:
        if char == '{':
            acc += char + '\\l' + ' ' * (tabsize + 4)
            tabsize += 4
        elif char == '}':
            acc += '\\l' + ' ' * (tabsize - 4) + char
            tabsize -= 4
        elif char == ',':
            acc += char + '\\l' + ' ' * tabsize
        elif char == ' ':
            pass
        else:
            acc += char
    return acc

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