def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b ให้ผลลัพธ์เป็น 0")
    else:
        print (c)
  

AbyB(6.0, 5.0)
AbyB(2.0, 5.0)
print ("โดย นางสาวพัชราภา แก้วมา")