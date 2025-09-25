import math, random

def OWT_door(x):
    x = int(x)
    arr = []
    temp = x
    while temp != 0:
        a = temp % 10
        temp = int(temp/10)
        arr.append(a)
    print(arr)
    t1 = x%7
    tn = 0
    for i in arr:
        t = i%2
        tn = tn*10 + t
    a = (str(arr[0]*21)+str(arr[4]*39)+str(arr[5]*46))
    b = (str(arr[1]*42)+str(arr[3]*69)+str(arr[2]*79))
    result = int(a+str(t1)+str(tn)+b)
    return result

def generateOTP():
 
    # Declare a digits variable  
    # which stores all digits 
    digits = "0123456789"
    OTP = ""
 
#    length of password can be changed
#    by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    # code = OWT_door(OTP)
 
    return OTP

# x=generateOTP()
# y=OWT_door(x)
# print(x)