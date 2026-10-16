"""A beginner-friendly command-line contact book.

Run with: python contact_book.py
Contacts are dictionaries stored in a list. Phone numbers stay as strings
so leading zeros and a country-code prefix are preserved.
"""

import json
from pathlib import Path


CONTACTS_FILE = Path(__file__).resolve().with_name("contacts.json")


def add_contact(contacts, name, phone, email=""):
    """Add a contact with a required name and phone; email is optional."""
    name = name.strip()
    phone = phone.strip()
    email = email.strip()
    if not name or not phone:
        raise ValueError("Name and phone number cannot be empty.")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    return contact


def view_contacts(contacts):
    """Display numbered contacts, or a message when the list is empty."""
    if not contacts:
        print("No contacts found.")
        return
    for number, contact in enumerate(contacts, start=1):
        print(f"{number}. {contact['name']} | {contact['phone']} | "
              f"{contact['email'] or 'No email'}")


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


def edit_contact(contacts, number, name, phone, email=""):
    """Replace details using the contact number displayed by view_contacts."""
    if number < 1 or number > len(contacts):
        raise ValueError("Choose a contact number from the list.")
    name = name.strip()
    phone = phone.strip()
    email = email.strip()
    if not name or not phone:
        raise ValueError("Name and phone number cannot be empty.")
    contact = {"name": name, "phone": phone, "email": email}
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
    """Save the contact list as readable JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)
        file.write("\n")
