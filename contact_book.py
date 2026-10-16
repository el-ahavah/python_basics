"""A beginner-friendly command-line contact book.

Run with: python contact_book.py
Contacts are dictionaries stored in a list. Phone numbers stay as strings
so leading zeros and a country-code prefix are preserved.
"""

import json
from pathlib import Path


CONTACTS_FILE = Path(__file__).resolve().with_name("contacts.json")
