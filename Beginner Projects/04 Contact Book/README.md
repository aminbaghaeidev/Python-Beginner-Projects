# Contact Book Application
<img src="https://cdn-icons-png.flaticon.com/512/6347/6347034.png"
height=200px width=200px>

A simple command-line contact management application written in Python that lets you store, view, search, update, and delete contacts — all in memory during the session.

## Features

- **Add contacts** — Store a contact's name, phone number, email, and address
- **Edit contacts** — Update one or more fields for an existing contact
- **View all contacts** — List every saved contact with their full details
- **Search contacts** — Look up a specific contact by name
- **Delete contacts** — Remove a contact from the book

## Getting Started

### Prerequisites

- Python 3.x

No third-party libraries are required.

### Running the App

```bash
python contact_book.py
```

## Usage

Once launched, you'll see an interactive menu:

```
--- Contact Book Application ---
1. Add contact
2. Edit contact
3. View contacts
4. Search contact
5. Delete contact
6. Quit
```

Enter the number corresponding to the action you want to perform and follow the prompts.

### Example

```
Enter the number of the option you want: 1

Enter contact name: Alice
Enter contact phone: 555-1234
Enter contact email: alice@example.com
Enter contact address: 123 Main St
Contact added successfully!
```

When editing a contact, you can leave any field blank to keep the existing value.

## Project Structure

```
contact_book.py
│
├── class ContactBook        # Core data model and logic
│   ├── add_contact()        # Add a new contact
│   ├── update_contact()     # Update an existing contact
│   ├── delete_contact()     # Remove a contact
│   ├── search_contacts()    # Look up a contact by name
│   ├── view_contacts()      # Display all contacts
│   └── _check_contact()     # Internal helper for existence checks
│
└── __main__ block           # CLI entry point and menu loop
```

## Limitations

- Contacts are stored **in memory only** — all data is lost when the application exits.
- Contacts are looked up by **exact name match** (case-sensitive).
- No input validation is performed on phone numbers or email addresses.

## Potential Improvements

- Persist contacts to a file (JSON or CSV) so data survives between sessions
- Add case-insensitive search
- Validate phone and email formats
- Support multiple phone numbers or emails per contact
