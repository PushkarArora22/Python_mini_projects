def add_contact(contacts):
    name = input("Enter name: ").strip()

    while True:
        phone = input("Enter phone number: ").strip()

        if phone.isdigit():
            break

        print("Please enter a valid phone number.")

    contacts.append([name, phone])
    print("Contact added successfully.\n")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts saved.\n")
        return

    print("\n--- Contact Book ---")

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} - {contact[1]}")

    print()


def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if contact[0].lower() == name:
            print(f"\nFound: {contact[0]} - {contact[1]}\n")
            found = True
            break

    if not found:
        print("\nContact not found.\n")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()

    for contact in contacts:
        if contact[0].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully.\n")
            return

    print("Contact not found.\n")


def main():
    contacts = []

    while True:
        print("=== Contact Book ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.\n")


if __name__ == "__main__":
    main()
