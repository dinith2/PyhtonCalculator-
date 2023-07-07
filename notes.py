import os

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

def retrieve_note():
    clear_screen()
    print("----- Retrieve Note -----")
    backup_file = "notes_backup.txt"
    original_file = "notes.txt"

    if not os.path.isfile(backup_file):
        print("No notes have been deleted.")
        input("\nPress Enter to continue...")
        return

    print("Deleted Notes:")
    with open(backup_file, "r") as backup:
        deleted_notes = backup.readlines()
        for i, note in enumerate(deleted_notes, start=1):
            print(f"{i}. {note.strip()}")

    try:
        line_number = int(input("Enter the line number of the note to retrieve: "))
        if line_number < 1 or line_number > len(deleted_notes):
            print("Invalid line number.")
            input("\nPress Enter to continue...")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("\nPress Enter to continue...")
        return

    note_to_retrieve = deleted_notes[line_number - 1]
    with open(original_file, "a") as original:
        original.write(note_to_retrieve)

    with open(backup_file, "w") as backup:
        remaining_notes = deleted_notes[:line_number - 1] + deleted_notes[line_number:]
        backup.writelines(remaining_notes)

    print("Note retrieved and added back to the notes.")
    input("\nPress Enter to continue...")

def main_menu():
    while True:
        clear_screen()
        print("----- Notes App -----")
        print("1. Show Notes")
        print("2. Add Note")
        print("3. Delete Notes")
        print("4. Retrieve Note")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

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
            retrieve_note()
            input("\nPress Enter to continue...")
        elif choice == "5":
            clear_screen()
            print("Exiting the Notes App. Goodbye!")
            break
        else:
            input("Invalid choice! Press Enter to try again...")

main_menu()
