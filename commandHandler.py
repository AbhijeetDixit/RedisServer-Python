from serialize import MESSAGETYPE
configFilePath = ".config"

def insertValue(key, val):
    fo = open(configFilePath,"a")
    pair = key + "=>" + val + "\n"
    fo.write(pair)
    fo.close()
    return

def retrieveValue(key):
    fo = open(configFilePath, "r")
    lines = fo.read()
    lstLines = lines.splitlines()
    fo.close()
    for l in lstLines:
        kvpair = l.split("=>")
        if kvpair[0] == key:
            outLst = [kvpair[1]]
            return outLst, MESSAGETYPE.ARRAY
    return ["ERR"], MESSAGETYPE.ERROR

def handleCommand(msg):
    if len(msg) <= 0:
        return ["OK"], MESSAGETYPE.ARRAY
    elif msg[0] == "PING":
        return ["PONG"], MESSAGETYPE.ARRAY
    elif msg[0] == "ECHO":
        return msg[1:], MESSAGETYPE.ARRAY
    elif msg[0] == "set":
        insertValue(msg[1], msg[2])
        return ["OK"],  MESSAGETYPE.ARRAY
    elif msg[0] == "get":
        return retrieveValue(msg[1])
    else:
        return ["OK"], MESSAGETYPE.ARRAY