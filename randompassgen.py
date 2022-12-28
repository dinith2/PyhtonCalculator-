import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase +string.digits +string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

passlength = int(input("enter password length\n"))
get_random_string(passlength)