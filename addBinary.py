#used to add two binary numbers
from operator import*

def addbin(num1,num2):
    intSum = int(num1, 2) + int(num2, 2) 
    result = bin(intSum)[2:]  
    print(result)

def subbin(num1,num2):
    intSum = int(num1, 2) - int(num2, 2) 
    result = bin(intSum)[2:]  
    print(result)

while(True):
    print ("1.to add")
    print ('2. to subract')
    print('3.exit')
    choice = int(input('> Enter your choice: '))
    if choice == 1:
        num1 = str(input("Enter 1st bin number"))
        num2 = str(input("Enter second bin number "))
        addbin(num1,num2)
    elif choice == 2:
        num1 = str(input("Enter 1st bin number"))
        num2 = str(input("Enter second bin number "))
        subbin(num1,num2)
    elif choice == 3:
        exit(0)







