"""
Contact Manager App

A beginner-friendly project demonstrating:
- Variable, user, input, typecasting
- Lists & dictionaries
- Loops & control flow
- functions & f-string
"""


contacts =[]

#add contacts


def add_contacts():
    """Add a new contact to the contact list"""
    name  = input("Please enter the name here ->")
    phone  = input("Please enter the phone no. here ->")
    email = input("Please enter the email here ->")

    contact_info = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact_info)
    print(f"Contact for >{name}< added Successfully ✅\n")

    #view contact
def view_contacts():
    """Display all saved contacts."""
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n==== Contact List ====")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()


def search_contact(search_name):
    """Search for a contact by name."""
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']}\n")
            return
        print("Contact not found.\n")


def delete_contact(name_to_delete):
    """Delete contact by name."""
    for contact in contacts:
        if contact["name"].lower() == name_to_delete.lower():
            contacts.remove(contact)
            print(f"Contact '{name_to_delete}' deleted successfully!\n")
            return
        print("Contact not found.\n")


while True:
        print("""
        ===== Contact Manager =====
        1. Add Contact
        2. View Contacts
        3. Search Contact
        4. Delete Contact
        5. Exit
        """)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # name = input("Enter name: ")
            # phone = input("Enter phone: ")
            # email = input("Enter email: ")
            add_contacts()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")
