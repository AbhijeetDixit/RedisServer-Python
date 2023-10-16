from deserialize import *

def TestSimpleString():
    print("Testing simple string")
    msg = "+Hello World\r\n"
    outMsg = deserialize(msg)
    if outMsg == "Hello World":
        print("\tTest passed")
    else:
        print("Test failed")

def TestSimpleInteger():
    print("Testing simple integer")
    msg = ":41\r\n"
    outMsg = deserialize(msg)
    if outMsg != 41:
        print("Test failed")
        return
    else:
        msg = ":-41\r\n"
        outMsg = deserialize(msg)
        if outMsg == -41:
            print("\tTest passed")
        else:
            print("Test failed")

def TestBoolean():
    print("Testing Boolean")
    msg = "#t\r\n"
    outMsg = deserialize(msg)
    if outMsg != True:
        print("Test failed")
        return
    else:
        msg = "#f\r\n"
        outMsg = deserialize(msg)
        if outMsg == False:
            print("\tTest passed")
        else:
            print("Test failed")

def TestEmptyArray():
    print("Testing Empty Array : ")
    msg = "*0\r\n"
    outMsg = deserialize(msg)
    if outMsg == []:
        print("\tTest passed")
    else:
        print("Test failed")

def TestNullArray():
    print("Testing Null Array : ")
    msg = "*-1\r\n"
    outMsg = deserialize(msg)
    if(outMsg is None):
        print("\tTest passed")
    else:
        print("Test Failed")

def TestIntegerOnlyArray():
    print("Testing Integer Only Array : ")
    msg = "*2\r\n:1\r\n:2\r\n"
    outMsg = deserialize(msg)
    if outMsg == [1,2]:
        print("\tTest passed")
    else:
        print("Test failed")

def TestSimpleStringArray():
    print("Testing Simple Array : ")
    msg = "*3\r\n+Hello\r\n+there!\r\n+world"
    outMsg = deserialize(msg)
    if outMsg == ["Hello", "there!", "world"]:
        print("\tTest passed")
    else:
        print("Test failed")

def TestBulkStringOnlyArray():
    print("Testing Bulk String Array : ")
    msg = "*3\r\n$5\r\nhello\r\n$6\r\nthere!\r\n$5\r\nworld\r\n"
    outMsg = deserialize(msg)
    if outMsg == ["hello", "there!", "world"]:
        print("\tTest passed")
    else:
        print("Test failed")

def TestBooleanArray():
    print("Testing Boolean Array : ")
    msg = "*2\r\n#t\r\n#f\r\n"
    outMsg = deserialize(msg)
    if outMsg == [True, False]:
        print("\tTest passed")
    else:
        print("Test failed")

if __name__ == "__main__":
    TestBooleanArray()
    TestBulkStringOnlyArray()
    TestEmptyArray()
    TestIntegerOnlyArray()
    TestNullArray()
    TestSimpleStringArray()
    TestSimpleString()
    TestSimpleInteger()
    TestBoolean()