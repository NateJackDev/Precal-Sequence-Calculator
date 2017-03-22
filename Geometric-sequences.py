import math

def sequence(a1, n, r):
    an = a1 * (r ** (n-1))
    print(float(an))
def ratio(an, a1, n):
    r = (an/a1) ** (1/(n-1))
    print(float(r))
def termNumber(an, a1, r):
    n = math.log((an/a1),r) + 1
    print(float(n))
def series(a1, r, n):
    s = a1 * ((1 - (r ** n))/(1 - r))
    print(float(s))
def infiniteseries(a1, r):
    s = a1/(1-r)
    print(float(s))

print("Here are your Options:\nPlease Only enter Decimals value as inputs\n [1] Find the term value\n [2] Find the ratio\n [3] Find the Term # \n [4] Find the Sum Notation \n [5] Find the Sum of and Infinate Notation")
choice = int(input("What are we finding: "))

if(choice == 1):
    a1 = float(input("What is the value of a1: "))
    n = float(input("What is the term # of the term value you want to find: "))
    r = float(input("What is the ratio: "))
    sequence(a1, n, r)
elif(choice == 2):
    an = float(input("What is the term value: "))
    a1 = float(input("What is the value of a1: "))
    n = float(input("What is the term #: "))
    ratio(an, a1, n)
elif(choice == 3):
    an = float(input("What is the term value: "))
    a1 = float(input("What is the value of a1: "))
    r = float(input("What is the ratio: "))
    termNumber(an, a1, r)
elif(choice == 4):
    a1 = float(input("What is the value of a1: "))
    r = float(input("What is the ratio: "))
    n = float(input("What is the term #: "))
    series(a1, r, n)
elif(choice == 5):
    a1 = float(input("What is the value of a1: "))
    r = float(input("What is the ratio: "))
    infiniteseries(a1, r)
else:
    print("Invalid")
