import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts, name, number):
    contacts[name] = number
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' removed successfully.")
    else:
        print(f"Contact '{name}' not found.")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Number: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}")
            print(f"Number: {number}")
            print("-------------------")

def main_menu():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. Search for a contact")
        print("4. Display all contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(contacts, name, number)
        elif choice == '2':
            name = input("Enter contact name: ")
            remove_contact(contacts, name)
        elif choice == '3':
            name = input("Enter contact name: ")
            search_contact(contacts, name)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main_menu()
