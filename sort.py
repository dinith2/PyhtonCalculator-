import sys

def menu():
    print("1.sort numbers ")
    print("2.find the avg and median ")
    print("3.exit")
    

    option = int(input("enter your option"))

    while option != 0:
        print("select option")
        if option == 1:
           sort_main()
            # Choose your side
        elif option == 2:
            avg_main()
            pass 
        elif option == 3:
            exit_main()
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
        answer = input("1.find the averge 2. find the median")
        if answer == '1':
            try:
                num1, num2, num3, num4, num5, num6 = input("enter 6 numbers ")
                number = [num1,num2,num3,num4,num5,num6] 
                avg = sum(number)/len(number)
                print(avg)
            except: 
                print("invalid")
                avg_main()
        if answer == '2':
            try:
                #normal code
                n_num = [1, 2, 3, 4, 5]
                n = len(n_num)
                n_num.sort()
  
                if n % 2 == 0:
                    median1 = n_num[n//2]
                    median2 = n_num[n//2 - 1]
                    median = (median1 + median2)/2
                else:
                    median = n_num[n//2]
                    print("Median is: " + str(median))

def exit_main()
while True: 
        Answer = input("are you sure you want to quit? yes or no")
        if Answer == 'yes':
            sys.exit()
        elif Answer == 'no':
            menu()
            pass
        else: 
            print("invalid")
            exit_main()
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

