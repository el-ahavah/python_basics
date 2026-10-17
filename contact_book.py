import json
from pathlib import Path


CONTACTS_FILE = Path(__file__).resolve().with_name("contacts.json")


def add_contact(contacts, name, phone_number, email=""):
    """Add a contact with a required name and phone number; email is optional."""
    name = name.strip()
    phone_number = phone_number.strip()
    email = email.strip()
    if not name or not phone_number:
        raise ValueError("Name and phone number cannot be empty.")
    contact = {"name": name, "phone": phone_number, "email": email}
    contacts.append(contact)
    return contact


# Previous version, kept for comparison:
# def view_contacts(contacts):
#     """Display numbered contacts, or a message when the list is empty."""
#     if not contacts:
#         print("No contacts found.")
#         return
#     for number, contact in enumerate(contacts, start=1):
#         print(f"{number}. {contact['name']} | {contact['phone']} | "
#               f"{contact['email'] or 'No email'}")


def view_contacts(contacts):
    """Display contacts using a simple loop and a counter."""
    if not contacts:
        print("No contacts found.")
        return

    number = 1

    for contact in contacts:
        print("Contact:", number)
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"] or "No email")
        print()

        number += 1


def search_contacts(contacts, query):
    """Return partial name or phone matches, ignoring letter case."""
    query = query.strip().lower()
    if not query:
        raise ValueError("Enter a name or phone number to search.")
    matches = []
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            matches.append(contact)
    return matches


def edit_contact(contacts, number, name, phone_number, email=""):
    """Replace details using the contact number displayed by view_contacts."""
    if number < 1 or number > len(contacts):
        raise ValueError("Choose a contact number from the list.")
    name = name.strip()
    phone_number = phone_number.strip()
    email = email.strip()
    if not name or not phone_number:
        raise ValueError("Name and phone number cannot be empty.")
    contact = {"name": name, "phone": phone_number, "email": email}
    contacts[number - 1] = contact
    return contact


def delete_contact(contacts, number):
    """Remove and return the contact with the displayed number."""
    if number < 1 or number > len(contacts):
        raise ValueError("Choose a contact number from the list.")
    return contacts.pop(number - 1)


def load_contacts(filename=CONTACTS_FILE):
    """Load contacts from JSON; a missing file means a new contact book."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        return []
    if not isinstance(contacts, list):
        raise ValueError("The contacts file must contain a list.")
    for contact in contacts:
        if not isinstance(contact, dict):
            raise ValueError("Each saved contact must be a dictionary.")
        for field in ("name", "phone", "email"):
            if field not in contact or not isinstance(contact[field], str):
                raise ValueError("Each contact needs name, phone and email strings.")
        if not contact["name"].strip() or not contact["phone"].strip():
            raise ValueError("Saved names and phone numbers cannot be empty.")
    return contacts


def save_contacts(contacts, filename=CONTACTS_FILE):
    """Write JSON to a temporary file, then replace the saved contact book."""
    filename = Path(filename)
    temporary_file = filename.with_name(filename.name + ".tmp")
    try:
        with open(temporary_file, "w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)
            file.write("\n")
        temporary_file.replace(filename)
    finally:
        if temporary_file.exists():
            temporary_file.unlink()


def main():
    """Run the menu and save each successful change before accepting it."""
    try:
        contacts = load_contacts()
    except (OSError, ValueError) as error:
        print(f"Cannot load contacts: {error}")
        print("Check contacts.json before restarting. It has not been changed.")
        return

    while True:
        try:
            print("\nCONTACT BOOK")
            print("1. Add contact\n2. View contacts\n3. Search contacts")
            print("4. Edit contact\n5. Delete contact\n6. Exit")
            choice = input("Choose an option: ").strip()
            # Work on a copy so a failed save leaves the current list unchanged.
            updated_contacts = contacts.copy()

            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email (optional): ")
                add_contact(updated_contacts, name, phone, email)
                message = "Contact added."
            elif choice == "2":
                view_contacts(contacts)
                continue
            elif choice == "3":
                matches = search_contacts(contacts, input("Name or phone: "))
                view_contacts(matches)
                continue
            elif choice in ("4", "5"):
                view_contacts(contacts)
                if not contacts:
                    continue
                selection = input("Contact number (Enter to cancel): ").strip()
                if not selection:
                    continue
                try:
                    number = int(selection)
                except ValueError:
                    raise ValueError("Enter a whole-number contact number.") from None
                if number < 1 or number > len(contacts):
                    raise ValueError("Choose a contact number from the list.")
                contact = contacts[number - 1]
                if choice == "4":
                    print("Press Enter to keep a value; type - to clear email.")
                    name = input(f"Name [{contact['name']}]: ").strip()
                    phone = input(f"Phone [{contact['phone']}]: ").strip()
                    email = input(f"Email [{contact['email']}]: ").strip()
                    if email == "-":
                        email = ""
                    elif not email:
                        email = contact["email"]
                    edit_contact(updated_contacts, number,
                                 name or contact["name"],
                                 phone or contact["phone"], email)
                    message = "Contact updated."
                else:
                    answer = input(f"Delete {contact['name']}? (yes/no): ")
                    if answer.strip().lower() != "yes":
                        print("Deletion cancelled.")
                        continue
                    delete_contact(updated_contacts, number)
                    message = "Contact deleted."
            elif choice == "6":
                print("Goodbye!")
                return
            else:
                print("Please choose an option from 1 to 6.")
                continue

            save_contacts(updated_contacts)
            contacts = updated_contacts
            print(message)
        except ValueError as error:
            print(error)
        except OSError as error:
            print(f"Could not save contacts: {error}")
            print("Your change was not applied. Please try again.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return


if __name__ == "__main__":
    main()
