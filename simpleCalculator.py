print("select operation")
print("1. Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
operator = input()
#adding
if operator == "1":
    num1 = input("enter number : ")
    num2 = input ("enter another number: ")
    result = float(num1) + float(num2)
    print(result)
#subrating 
elif operator == "2":
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

