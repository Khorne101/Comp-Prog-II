x = int(input("Please type the value of integer x:"));
y = int(input("Please type the value of integer y:"));
z = int(input("Please type the value of integer z:"));
xodd = yodd = zodd = False;
def printx():
    print("Smallest odd number x:" + str(x));
def printy():
    print("Smallest odd number y:" + str(y));
def printz():
    print("Smallest odd number z:" + str(z));
if ((x%2 != 0) or (y%2 != 0) or (z%2 != 0)):
    if (x%2 != 0):
        if ((y%2 != 0) and (z%2 != 0)):
            if ((z<x) and (z<y)):
                printz();
            elif ((y<x) and (y<z)):
                printy();
            else:
                printx();
        elif (y%2 != 0):
            if (y<x):
                printy();
            else:
                printx();
        elif (z%2 != 0):
            if (z<x):
                printz();
            else:
                printx();
        else:
            printx();
    elif (y%2 != 0):
        if (z%2 != 0):
            if (z<y):
                printz();
            else:
                printy();
        else:
            printy();
    else:
        printz();
else: 
    print("None of the integers are odd.")