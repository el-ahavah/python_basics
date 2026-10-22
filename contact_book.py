import json
from pathlib import Path


CONTACTS_FILE = Path(__file__).resolve().with_name("contacts.json")


def add_contact(contacts, name, phone_number, email=""):
    """Add a contact with a required name and phone number; email is optional."""
    name = name.strip()
    phone_number = phone_number.strip()
    email = email.strip()
    if not name or not phone_number:
        raise ValueError("Please enter both a name and a phone number. Nothing was changed.")
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
        print("\nThere are no contacts to show yet.")
        print("Choose 1 from the main menu to add your first contact.")
        return

    print("\nCONTACT LIST")
    print("Number of contacts shown:", len(contacts))
    number = 1

    for contact in contacts:
        print("-" * 44)
        print("Contact number:", number)
        print("Name:          ", contact["name"])
        print("Phone number:  ", contact["phone"])
        print("Email address: ", contact["email"] or "Not provided")
        number += 1

    print("-" * 44)


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
        raise ValueError("Please choose one of the contact numbers shown in the list.")
    name = name.strip()
    phone_number = phone_number.strip()
    email = email.strip()
    if not name or not phone_number:
        raise ValueError("Please enter both a name and a phone number. Nothing was changed.")
    contact = {"name": name, "phone": phone_number, "email": email}
    contacts[number - 1] = contact
    return contact


def delete_contact(contacts, number):
    """Remove and return the contact with the displayed number."""
    if number < 1 or number > len(contacts):
        raise ValueError("Please choose one of the contact numbers shown in the list.")
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


def save_contacts(contacts, filename=CONTACTS_FILE):  # Receive the contacts and use the default save location unless another is provided.
    """Write JSON to a temporary file, then replace the saved contact book."""  # Describe what this function does.
    filename = Path(filename) # Convert the filename into a Path object so we can use file-related methods.
    temporary_file = filename.with_name(filename.name + ".tmp") # Choose a temporary file in the same folder, such as contacts.json.tmp.

    try: # Attempt the saving steps below; the finally block will run afterward even if an error occurs.
        with open(temporary_file, "w", encoding="utf-8") as file: # Open the temporary file for writing; close it automatically when this block ends.
            json.dump(contacts, file, indent=4, ensure_ascii=False) # Save the contacts as JSON, using four-space indentation and keeping characters such as é readable.
            file.write("\n") # Add a newline after the saved JSON.

        temporary_file.replace(filename) # Replace the main contacts file with the completed temporary file.

    finally: # Run the following cleanup whether saving succeeds or fails.
        if temporary_file.exists(): # Check whether the temporary file still exists.
            temporary_file.unlink() # Delete the remaining temporary file.


def main():
    """Run the menu and save each successful change before accepting it."""
    try:
        contacts = load_contacts()
    except OSError:
        print("\nYour saved contacts could not be opened.")
        print("Check that you have permission to open the saved contacts file, then try again.")
        print("Your saved contacts have not been changed.")
        return
    except ValueError:
        print("\nThe saved contacts file could not be read because its contents are damaged or incomplete.")
        print("Your file has not been changed. Restore a backup or ask someone to help repair it.")
        return

    print("\nWelcome to your Contact Book!")
    print("Keep the names, phone numbers and email addresses of people you know.")
    print("Your contacts are saved automatically after each change.")

    while True:
        try:
            print("\n" + "=" * 44)
            print("CONTACT BOOK - MAIN MENU")
            print("=" * 44)
            print("1. Add a new contact")
            print("2. Show all contacts")
            print("3. Find a contact")
            print("4. Change a contact's details")
            print("5. Remove a contact")
            print("6. Close the contact book")
            print()
            choice = input("Type a number from 1 to 6, then press Enter: ").strip()
            # Work on a copy so a failed save leaves the current list unchanged.
            updated_contacts = contacts.copy()

            if choice == "1":
                print("\nADD A NEW CONTACT")
                print("A name and phone number are required.")
                print("You can leave the email address blank.")
                name = input("Person's name: ")
                phone_number = input("Phone number (include any starting zeros or +): ")
                email = input("Email address (press Enter to skip): ")
                add_contact(updated_contacts, name, phone_number, email)
                message = f"Saved! {name.strip()} has been added to your contact book."
            elif choice == "2":
                view_contacts(contacts)
                continue
            elif choice == "3":
                if not contacts:
                    view_contacts(contacts)
                    continue
                print("\nFIND A CONTACT")
                print("Type all or part of a name or phone number.")
                print("For phone numbers, use the same spacing as the saved number.")
                query = input("Search for (press Enter to return to the menu): ").strip()
                if not query:
                    print("Search cancelled. Returning to the main menu.")
                    continue
                matches = search_contacts(contacts, query)
                if matches:
                    print("\nSearch results for:", query)
                    view_contacts(matches)
                    print("To change or remove a contact, choose 4 or 5 from the main menu.")
                else:
                    print("No contacts matched your search. Try another name or number.")
                continue
            elif choice in ("4", "5"):
                view_contacts(contacts)
                if not contacts:
                    continue
                print("Use the contact number shown above, not the person's phone number.")
                selection = input("Contact number (press Enter to return to the menu): ").strip()
                if not selection:
                    print("No changes made. Returning to the main menu.")
                    continue
                try:
                    number = int(selection)
                except ValueError:
                    raise ValueError("Type the contact number as digits, for example 1 or 2.") from None
                if number < 1 or number > len(contacts):
                    raise ValueError("Please choose one of the contact numbers shown in the list.")
                contact = contacts[number - 1]
                if choice == "4":
                    print("\nCHANGE CONTACT DETAILS")
                    print("You are changing:", contact["name"])
                    print("The current details appear in brackets.")
                    print("Press Enter without typing to keep a detail.")
                    print("To remove the email address, type just - and press Enter.")
                    name = input(f"New name [{contact['name']}]: ").strip()
                    phone_number = input(f"New phone number [{contact['phone']}]: ").strip()
                    email = input(f"New email address [{contact['email'] or 'Not provided'}]: ").strip()
                    if email == "-":
                        email = ""
                    elif not email:
                        email = contact["email"]
                    edit_contact(updated_contacts, number,
                                 name or contact["name"],
                                 phone_number or contact["phone"], email)
                    message = f"Saved! The details for {updated_contacts[number - 1]['name']} have been updated."
                else:
                    print("\nREMOVE A CONTACT")
                    print("Name:", contact["name"])
                    print("Phone number:", contact["phone"])
                    print("This will remove the contact from your saved contact book.")
                    answer = input("Type yes to remove this contact, or press Enter to keep it: ")
                    if answer.strip().lower() != "yes":
                        print("Contact kept. Nothing was removed.")
                        continue
                    delete_contact(updated_contacts, number)
                    message = f"Removed {contact['name']} from your contact book."
            elif choice == "6":
                print("Your saved contacts will be here next time. Goodbye!")
                return
            else:
                print("That option is not on the menu. Type a number from 1 to 6.")
                continue

            save_contacts(updated_contacts)
            contacts = updated_contacts
            print(message)
        except ValueError as error:
            print(error)
        except OSError:
            print("\nWe could not save this change, so it has not been applied.")
            print("Check that you have free storage space and permission to save files here.")
            print("Your earlier saved contacts are still available. Try again when ready.")
        except (EOFError, KeyboardInterrupt):
            print("\nClosing the contact book. Only completed, saved changes have been kept.")
            return


if __name__ == "__main__":
    main()
