def parseArray(msg):
    lst = msg.splitlines() #splitting on \r\n
    lst = [l for l in lst if l != ''] #removing empty values
    outlst = [] #output list
    lst[0] = lst[0][1:]
    #print(lst)
    if int(lst[0]) == 0:
        return outlst
    elif int(lst[0]) == -1:
        return None
    else:
        cnt = 1
        while cnt < len(lst):
            #print("cnt = ", cnt)
            #print(lst[cnt])
            if lst[cnt][0] == "$":
                outlst.append(parseBulkString(lst[cnt:cnt+2]))
                cnt =cnt + 2
            else:
                outlst.append(deserialize(lst[cnt]))
                cnt = cnt + 1
    return outlst

def parseBulkString(msg):
    if isinstance(msg, str):
        msg = msg.splitlines()
    s = msg[1].rstrip()
    return s

def parseString(msg):
    return msg[1:].rstrip()

def parseInteger(msg):
    msg = msg[1:]
    return int(msg)

def parseBoolean(msg):
    if msg[1] == 't':
        return True
    return False

def deserialize(msg):
    if len(msg) < 1:
        return ""
    if msg[0] == "*":
        return parseArray(msg)
    elif msg[0] == "+":
        return parseString(msg)
    elif msg[0] == ":":
        return parseInteger(msg)
    elif msg[0] == "#":
        return parseBoolean(msg)
    elif msg[0] == "$":
        return parseBulkString(msg)