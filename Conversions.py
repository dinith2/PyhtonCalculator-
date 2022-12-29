#this code is used for conversion between binary and deicmal

def mainmenu():
    while(True):
        print ('1. bin to dec')
        print ('2. dec to bin')
        print('3.exit')
        choice = int(input('> Enter your choice: '))

    
        if choice == 1:
            print ('Starting Scan\n')
            binCon()

        elif choice == 2:
            print ('Starting Ping\n')
        elif choice == 3:
            print ('Exiting\n')
            exit(0)
        else:
            mainmenu(6)


def binCon():
    print("")
    

mainmenu()

   







