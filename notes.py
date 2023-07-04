import os

def retrive_note():
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_notes():
    clear_screen()
    print("----- Notes -----")
    with open("notes.txt", "r") as file:
        notes = file.read()
        print(notes)

def add_note():
    clear_screen()
    print("----- Add Note ----")
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("---Note added successfully!--")

def delete_notes():
    clear_screen()
    print("----- Delete Notes -----")
    confirmation = input("Are you sure you want to delete all notes? (y/n): ")
    if confirmation.lower() == "y":
        with open("notes.txt", "w") as file:
            file.write("")
        print("All notes deleted.")
    else:
        print("Deletion canceled.")

def main_menu():
    while True:
        clear_screen()
        print("----- Notes App -----")
        print("1. Show Notes")
        print("2. Add Note")
        print("3. Delete Notes")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_notes()
            input("\nPress Enter to continue...")
        elif choice == "2":
            add_note()
            input("\nPress Enter to continue...")
        elif choice == "3":
            delete_notes()
            input("\nPress Enter to continue...")
        elif choice == "4":
            clear_screen()
            print("Exiting the Notes App. Goodbye!")
            break
        else:
            input("Invalid choice! Press Enter to try again...")

# Run the Notes App
main_menu()