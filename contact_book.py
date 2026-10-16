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
