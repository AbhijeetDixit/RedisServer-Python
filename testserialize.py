from serialize import *
from deserialize import *

def TestSimpleString():
    print("Testing simple string")
    msg = "Hello World"
    outMsg = serialize(msg, MESSAGETYPE.STRING)
    reMsg = deserialize(outMsg)
    if reMsg == msg:
        print("\t\tTest passed")
    else:
        print("Test failed")

def TestBoolean():
    print("Testing boolean value")
    msg = True
    outMsg = serialize(msg, MESSAGETYPE.BOOLEAN)
    reMsg = deserialize(outMsg)
    if reMsg == msg:
        print("\t\tTest passed")
    else:
        print("Test failed")

def TestInteger():
    print("Testing simple integer")
    msg = 38
    outMsg = serialize(msg, MESSAGETYPE.INTEGER)
    reMsg = deserialize(outMsg)
    if reMsg != msg:
        print("Test Failed")
        return
    else:
        msg = -38
        outMsg = serialize(msg, MESSAGETYPE.INTEGER)
        reMsg = deserialize(outMsg)
        if reMsg == msg:
            print("\t\tTest Passed")
        else:
            print("test failed")

def TestBulkString():
    print("Testing Bulk String")
    msg = "hello"
    outMsg = serialize(msg, MESSAGETYPE.BULKSTRING)
    reMsg = deserialize(outMsg)
    if reMsg == msg:
        print("\t\tTest passed")
    else:
        print("test failed")

def TestArray():
    print("Testing Array ")
    msg = ["Hello", "World"]
    outMsg = serialize(msg, MESSAGETYPE.ARRAY)
    reMsg = deserialize(outMsg)
    if reMsg == msg:
        print("\t\ttest passed")
    else:
        print("test failed")

def TestError():
    print("Testing error value")
    msg = "WRONGTYPE"
    outMsg = serialize(msg, MESSAGETYPE.ERROR)
    if outMsg == "-WRONGTYPE Operation against a key holding the wrong kind of value\r\n":
        print("\t\ttest passed")
    else:
        print("test failed")

if __name__ == "__main__":
    TestArray()
    TestBoolean()
    TestBulkString()
    TestError()
    TestInteger()
    TestSimpleString()