import numpy
import math 

print("select operation")
print("1. Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.trig function")
print("test")
print("6.exit")

operator = input()
#adding
if operator == "1":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) + float(num2)
    print(result)
#subrating 
elif operator == "2" or "add":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) - float(num2)
    print(result)
#multiplying
elif operator == "3":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) * float(num2)
    print(result)
#dividing
elif operator == "4":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) // float(num2)
    print(result)

else:
    print("invalid")

def main():
    
    trig = input('calculate sin cosine or tan')
    if trig =='sin' or trig == 'sin':
        a = eval(input('what is the angle measure'))
        result = math.sin(math.radians(a))
        print('the answer is '+str(round,3))
        main()
    else:
            print('invalid')
