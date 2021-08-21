a = 83
def Function():
    global a
    print("Global variable",a)
    a+=5 #Local variable of function
    print(a)

Function()
print(a)
