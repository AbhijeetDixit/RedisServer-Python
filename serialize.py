from enum import Enum
from errors import *

class MESSAGETYPE(Enum):
    ARRAY = 1,
    BULKSTRING = 2,
    INTEGER = 3,
    BOOLEAN = 4,
    STRING = 5,
    ERROR = 6

def serializeArray(msg):
    if type(msg) is not list:
        return None
    out = "*" + str(len(msg)) + "\r\n"
    for m in msg:
        if isinstance(m, str):
            out = out + serializeString(m)
        elif isinstance(m, int):
            out = out + serializeInteger(m)
        elif isinstance(m, bool):
            out = out + serializeBoolean(m)
    return out
    

def serializeError(msg):
    if not isinstance(msg, str):
        return ""
    out = ""
    if msg not in ErrorDict.keys():
        out = "-ERR " + ErrorDict["ERR"] + "\r\n"
    else:
        out = "-" + msg
        out = out + " " + ErrorDict[msg] + "\r\n"
    return out

def serializeInteger(msg):
    if not isinstance(msg, int):
        return None
    out = ":" + str(msg) + "\r\n"
    return out

def serializeString(msg):
    if not isinstance(msg, str):
        msg = str(msg)
    out = "+" + msg + "\r\n"
    return out

def serializeBulkString(msg):
    if not isinstance(msg, str):
        msg = str(msg)
    out = "$"
    out = out + str(len(msg))
    out = out + "\r\n" + msg + "\r\n"
    return out

def serializeBoolean(msg):
    if not isinstance(msg, bool):
        return None
    out = "#"
    if msg == True:
        out = out + "t" + "\r\n"
    else:
        out = out + "f" + "\r\n"
    return out

def serialize(msg, msgType):
    if msgType not in MESSAGETYPE:
        return None
    if msgType.name == MESSAGETYPE.ARRAY.name:
        return serializeArray(msg)
    elif msgType.name == MESSAGETYPE.BOOLEAN.name:
        return serializeBoolean(msg)
    elif msgType.name == MESSAGETYPE.BULKSTRING.name:
        return serializeBulkString(msg)
    elif msgType.name == MESSAGETYPE.ERROR.name:
        return serializeError(msg)
    elif msgType.name == MESSAGETYPE.INTEGER.name:
        return serializeInteger(msg)
    elif msgType.name == MESSAGETYPE.STRING.name:
        return serializeString(msg)
    else:
        return None