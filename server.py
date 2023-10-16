import socket
from deserialize import *
from serialize import *
from commandHandler import *

"""def getReplyMessage():
    msg = "*1\r\n$4\r\nPONG\r\n"
    return msg"""

"""def serializeMessage(msg):
    print("unserialized message : ", msg)
    lst = msg.splitlines()
    print(len(lst))
    if len(lst) < 0:
        return "empty"
    if len(lst) == 1:
        return "empty"
    else:
        finalMsg = ""
        cnt = 2
        while cnt < len(lst):
            finalMsg = finalMsg + lst[cnt]
            cnt = cnt + 2
        return finalMsg"""

if __name__ == "__main__":
    s = socket.socket()
    #print("Socket created successfully")

    port = 6379
    s.bind(('', port))
    #print("Socket binded to "+ str(port))

    s.listen(5)
    #print("socket is listening")

    while True:
        #print("Trying to accept")
        c,addr = s.accept()
        #print("Got a connection from ", addr)

        msg = ""

        while True:
            #print("Connected")
            msg = c.recv(1024).decode()
            #print("Got message : ", msg)
            parsedMsg = deserialize(msg)
            #print("recieved ", parsedMsg)
            out,type = handleCommand(parsedMsg)
            c.send(serialize(out,type).encode())
            break
        break