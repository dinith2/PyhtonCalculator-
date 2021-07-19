

def menu():
    print("1.sort numbers ")
    print("2.find the avg ")
    

    option = int(input("enter your option"))

    while option != 0:
        print("select option")
        if option == 1:
           sort_main()
            # Choose your side
        elif option == 2:
            print("hi")
            pass 
        elif option == 3:
            print("hi")
            pass 
        else:
            print("invalid")
            menu()

def sort_main():
     while True:
        Answer = input("1. decrease  2. increase ")
        if Answer == '1':

            try:
                num1, num2, num3, num4, num5, num6, num7 = input("enter 7 numbers").split()
                my_list = [num1, num2, num3, num4, num5, num6, num7]
            except: 
                print("invalid, only print numbers ")
                sort_main()
                #sort in decreasing order
                my_list = sorted(my_list, reverse=True) 
                print(my_list)
            
               
        elif Answer == '2':
            try:
                num1, num2, num3, num4, num5, num6, num7 = input("enter 7 numbers").split()
                my_list=[num1, num2, num3, num4, num5, num6, num7]
            except:
                print("invalid, only print numbers")
                sort_main()
                # sort in increasing order
                my_list = sorted(my_list, reverse=False) 
                print(my_list)
            
            pass
        else: 
            print("invalid")
            sort_main()
            print("go back to menu")

            break 

def avg_main(): 
    while True: 
        answer = 

    



menu()






# sort in decreasing order
#my_list = sorted(my_list, reverse=True) 
#print(my_list)

# sort in increasing order
#my_list = sorted(my_list, reverse=False) 
#print(my_list)

# another way to sort using built-in methods
#my_list.sort(reverse=True)  
#print(my_list)

# sort again using slice indexes
#print(my_list[::-1])

