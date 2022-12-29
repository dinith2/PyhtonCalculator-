#used to add two binary numbers
from operator import*

def addbin(num1,num2):
    intSum = int(num1, 2) + int(num2, 2) 
    result = bin(intSum)[2:]  
    print(result)

num1 = str(input("Enter 1st bin number"))
num2 = str(input("Enter second bin number "))
addbin(num1,num2)

