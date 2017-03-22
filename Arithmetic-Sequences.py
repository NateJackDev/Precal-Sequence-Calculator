def sequence(a1, n, d):
    an = a1 + (d*(n-1))
    print(an)
def differance(an, a1, n):
    d = (an - a1)/(n-1)
    print(float(d))
def sumNotation(a1, an, n):
    s = (n/2)*(a1+an)
    print(s)

print("Here are your Options:\n [1] Find the term value(a_)\n [2] Find the difference in term values\n [3] Find the Sum Notation \n")
choice = int(input("What are we finding: "))

if(choice == 1):
    a1 = float(input("What is the value of a1: "))
    n = float(input("What is the term number you are finding: "))
    d = float(input("What is the difference: "))
    sequence(a1, n, d)
elif(choice == 2):
    an = float(input("What is the term value: "))
    a1 = float(input("What is the value of a1: "))
    n = float(input("What is the term number: "))
    differance(an, a1, n)
elif(choice == 3):
    n = float(input("What is the term number: "))
    a1 = float(input("What is the value of a1: "))
    an = float(input("What is the term value: "))
    sumNotation(a1, an, n)
else:
    print("Invalid")
