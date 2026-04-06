# NOTE problem 1
import math as m;

def recursive(x):
    if (x == 0):
        return m.sqrt(m.pi)
    else:
        return (((2 * x - 1) * recursive(x-1))/2)
    

# NOTE problem 2
def p2(x,k):
    total = 0.0;
    for n in range(k-1):
        total = total + (
            (((-1)**n) * (x**((2*n) + 1)))
            /
            (m.factorial(n) * ((2*n) + 1))
        )
    total = total * (2/m.sqrt(m.pi))
    return total


# NOTE problem 3
def p3(filename, word):
    file = open(filename)
    word = str.lower(word)
    counter = 0
    for line in file:
        lineArr = str.split(line, "")

