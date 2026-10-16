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
