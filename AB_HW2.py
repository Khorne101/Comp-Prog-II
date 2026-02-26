s = input("Please input your numbers:");
finalNumber = 0.0;
i = 0;
ii = 0;
def numberFunc(i, nextComma, s):
    j = i;
    currentStr = "";
    while (j < nextComma):
        currentStr += s[j];
        j += 1;
    return float(currentStr)
while (i < len(s)): 
    nextComma = str.find(s, ",", i+1);
    if ((nextComma > 0)):
        finalNumber += numberFunc(i, nextComma, s)
        i = nextComma + 1;
    elif (nextComma == -1):
        finalNumber += numberFunc(i, len(s), s)
        i = len(s);
    else:
        i = len(s);
    ii += 1;
print("final sum: " + str(finalNumber))