print("select operation")
print("1. Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
operator = input()
#adding
if operator == "1" or "Add":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) + float(num2)
    print(result)
#subrating 
elif operator == "2" or "subtract":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) - float(num2)
    print(result)
#multiplying
elif operator == "3" or "multiply":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) * float(num2)
    print(result)
#dividing
elif operator == "4" or "divide":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) // float(num2)
    print(result)

else:
    print("invalid")

