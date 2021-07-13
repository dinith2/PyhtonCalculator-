

def menu():
    print("1.sort numbers ")
    

    option = int(input("enter your option"))

    while option != 0:
        print("select option")
        if option == 1:
           dtin_main()
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

def dtin_main():
     while True:
        print("2.decreasing to increasing")
        Answer = input("enter your option ")
        if Answer == '2':
            my_list = [5, 3, 1, 2, 4, 7, 6]
            #sort in decreasing order
            my_list = sorted(my_list, reverse=True) 
            print(my_list)   
        elif Answer == '1':
            my_list = [5, 3, 1, 2, 4, 7, 6]
            # sort in increasing order
            my_list = sorted(my_list, reverse=False) 
            print(my_list)
            pass
        else: 
            print("invalid")

            break 

    



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

