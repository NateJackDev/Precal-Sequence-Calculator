import math

def Arthsequence(a1, n, d):
    an = a1 + (d*(n-1))
    print(an)
def Arthdifferance(an, a1, n):
    d = (an - a1)/(n-1)
    print(float(d))
def ArthsumNotation(a1, an, n):
    s = (n/2)*(a1+an)
    print(s)
def Geosequence(a1, n, r):
    an = a1 * (r ** (n-1))
    print(float(an))
def Georatio(an, a1, n):
    r = (an/a1) ** (1/(n-1))
    print(float(r))
def GeotermNumber(an, a1, r):
    n = math.log((an/a1),r) + 1
    print(float(n))
def Geoseries(a1, r, n):
    s = a1 * ((1 - (r ** n))/(1 - r))
    print(float(s))
def Geoinfiniteseries(a1, r):
    s = a1/(1-r)
    print(float(s))
try:
    print("Hello, I am a calculator for Arithmetic and Geometric Sequences and Series")
    print("Here are your Options:\n [ 1 ] Arithmetic\n [ 2 ] Geometric")
    choice = int(input("What are we Solving: "))
    if(choice == 1):
        print("\nHere are your Options:\n [ 1 ] Find the term value(a_)\n [ 2 ] Find the difference in term values\n [ 3 ] Find the Sum Notation \n")
        choiceArth = int(input("What are we finding: "))
        if(choiceArth == 1):
            a1 = float(input("What is the value of a1: "))
            n = float(input("What is the term number you are finding: "))
            d = float(input("What is the difference: "))
            Arthsequence(a1, n, d)
        elif(choiceArth == 2):
            an = float(input("What is the term value: "))
            a1 = float(input("What is the value of a1: "))
            n = float(input("What is the term number: "))
            Arthdifferance(an, a1, n)
        elif(choiceArth == 3):
            n = float(input("What is the term number: "))
            a1 = float(input("What is the value of a1: "))
            an = float(input("What is the term value: "))
            ArthsumNotation(a1, an, n)
        else:
            print("Invalid")
    elif(choice == 2):
        print("\nHere are your Options:\nPlease Only enter Decimals value as inputs\n [ 1 ] Find the term value\n [ 2 ] Find the ratio\n [ 3 ] Find the Term # \n [ 4 ] Find the Sum Notation \n [ 5 ] Find the Sum of and Infinate Notation")
        choiceGeo = int(input("What are we finding: "))
        if(choiceGeo == 1):
            a1 = float(input("What is the value of a1: "))
            n = float(input("What is the term # of the term value you want to find: "))
            r = float(input("What is the ratio: "))
            Geosequence(a1, n, r)
        elif(choiceGeo == 2):
            an = float(input("What is the term value: "))
            a1 = float(input("What is the value of a1: "))
            n = float(input("What is the term #: "))
            Georatio(an, a1, n)
        elif(choiceGeo == 3):
            an = float(input("What is the term value: "))
            a1 = float(input("What is the value of a1: "))
            r = float(input("What is the ratio: "))
            GeotermNumber(an, a1, r)
        elif(choiceGeo == 4):
            a1 = float(input("What is the value of a1: "))
            r = float(input("What is the ratio: "))
            n = float(input("What is the term #: "))
            Geoseries(a1, r, n)
        elif(choiceGeo == 5):
            a1 = float(input("What is the value of a1: "))
            r = float(input("What is the ratio: "))
            Geoinfiniteseries(a1, r)
        else:
            print("Invalid")
except NameError:
    print("\nThat's not a Option!")
except KeyboardInterrupt:
    print("\nSee Ya!")
