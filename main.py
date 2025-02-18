# Simple Calculator

def add(a,b):
    return a + b

def subs(a,b):
    return a - b

def multi(a,b):
    return a * b

def divide(a,b):
    return a / b

num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))

print("Sum :", add(num1 , num2))
print("Difference :", subs(num1 , num2))
print("Product :", multi(num1 , num2))
print("Quotient :", divide(num1 , num2))