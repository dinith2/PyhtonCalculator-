import math 
import numpy 
from fractions import Fraction 

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

#sin 
print('\nTrigonometric SINE')


sine_radians = math.sin(0.523599)


print('sine of 0.523599 radians (30 degrees) is', sine_radians, 'rounded', round(sine_radians, 2))



sine_degrees = math.sin(math.radians(30))


print('sine of 30 degrees is', sine_degrees, 'rounded', round(sine_degrees, 2))



print('sine of 30 degrees ratio is', Fraction(sine_degrees).limit_denominator())



sine_with_numpy = numpy.sin(numpy.deg2rad(30))
print('sine of 30 degrees using numpy is', Fraction(sine_with_numpy).limit_denominator())


else:
    print("invalid")

