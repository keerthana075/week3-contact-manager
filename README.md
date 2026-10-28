# Contact Management System

## Project Description

A comprehensive Contact Management System built with Python using dictionaries and functions. This system allows users to manage their contacts with full CRUD operations (Create, Read, Update, Delete), search functionality, input validation, and data persistence.

The application stores contact information such as names, phone numbers, email addresses, addresses, and groups. It also supports JSON file storage, CSV export, contact statistics, and backup functionality.

## What I Learned

1. **Functions:** Creating reusable and organized code blocks for different operations.
2. **Dictionaries:** Storing and retrieving data using key-value pairs and nested dictionaries.
3. **String Methods:** Using `strip()` and `lower()` to clean and compare text.
4. **File Operations:** Saving and loading contact information using JSON files.
5. **Input Validation:** Validating phone numbers, email addresses, and user input.
6. **Error Handling:** Handling unexpected situations and file errors gracefully.
7. **CSV Files:** Exporting contact information into a CSV file.
8. **Date and Time:** Recording when contacts are created and updated.
9. **Testing:** Checking functions using automated tests and different inputs.

## Features

- Add new contacts with validation
- Search contacts by name with partial matching
- Search contacts by phone number
- Update existing contact information
- Delete contacts with confirmation
- View all contacts in a formatted display
- Validate phone numbers and email addresses
- Save contacts to a JSON file automatically
- Load saved contacts when the program starts
- Export contacts to CSV format
- View contact statistics and group counts
- Identify contacts updated within the last seven days
- Create a backup of saved contacts
- Handle invalid menu choices and file errors
- Prevent duplicate contact names

## Technologies Used

- **Programming Language:** Python
- **Data Structure:** Dictionaries
- **Data Storage:** JSON
- **Data Export:** CSV
- **Testing:** Python `unittest` module
- **Modules:** `json`, `re`, `csv`, `os`, `shutil`, `datetime`, and `unittest`

## Project Structure

```text
week3-contact-manager/
│
├── contacts_manager.py
├── contacts_data.json
├── test_contacts.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── contacts_backup.json
└── contacts_export.csv
```

**Note:** `contacts_backup.json` and `contacts_export.csv` are generated when you use the backup and export features. They do not need to exist before the first run.

## Requirements

- Python 3.8 or newer
- Visual Studio Code or another Python editor
- No external packages are required

## How to Run

### Step 1: Open the Project Folder

Open the `week3-contact-manager` folder in Visual Studio Code.

### Step 2: Open the Terminal

Select **Terminal → New Terminal**.

### Step 3: Run the Program

```bash
python contacts_manager.py
```

The program will load saved contacts from `contacts_data.json`. If the file does not exist, it starts with an empty contact dictionary.

## How to Run Automated Tests

Run the following command in the terminal:

```bash
python -m unittest -v test_contacts.py
```

The tests check phone validation, email validation, partial name search, phone search, adding contacts, updating contacts, deleting contacts, and JSON file operations.

## Data Structure

Contacts are stored in a dictionary. Each contact name is a key, and its information is stored in a nested dictionary.

Example:

```python
contacts = {
    "John Doe": {
        "phone": "919876543210",
        "email": "john@gmail.com",
        "address": "123 Main Street",
        "group": "Friends",
        "created_at": "2026-10-28T10:00:00",
        "updated_at": "2026-10-28T10:00:00"
    },
    "ravi": {
        "phone": "9876543210",
        "email": "ravi@gmail.com",
        "address": "123 Main Street",
        "group": "Work",
        "created_at": "2026-10-28T10:00:00",
        "updated_at": "2026-10-28T10:00:00"
    }
}
```

## Main Menu

The program displays the following menu:

```text
==================================================
       CONTACT MANAGEMENT SYSTEM
==================================================

==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Create Backup
9. Exit
==============================

Enter your choice (1-9):
```

## Sample Output

### Adding a Contact

```text
Enter your choice (1-9): 1

--- ADD NEW CONTACT ---
Enter contact name: John Doe
Enter phone number: +91 98765 43210
Enter email (optional, press Enter to skip): john@example.com
Enter address (optional): 123 Main Street
Enter group (Friends/Work/Family/Other): Friends

Contact 'John Doe' added successfully!
Contacts saved to contacts_data.json
```

### Searching for a Contact

```text
Enter your choice (1-9): 2

--- SEARCH CONTACT ---
1. Search by name
2. Search by phone number
Enter choice (1-2): 1
Enter name to search: john

Found 1 contact(s)
--------------------------------------------------
1. John Doe
   Phone: 919876543210
   Email: john@example.com
   Address: 123 Main Street
   Group: Friends
--------------------------------------------------
```

### Viewing Statistics

```text
--- CONTACT STATISTICS ---
Total Contacts: 1

Contacts by Group:
  Friends: 1 contact(s)

Recently Updated (last 7 days): 1
```

*The output depends on the contacts stored in your file and their update dates.*

## Challenges and Solutions

### 1. Handling Duplicate Contact Names

**Challenge:** Users may try to add a contact with a name that already exists.

**Solution:** The program checks whether the name exists before adding a new contact and offers an option to update the existing contact.

### 2. Phone Number Validation

**Challenge:** Phone numbers may contain spaces, plus signs, brackets, or hyphens.

**Solution:** The program uses regular expressions to remove non-digit characters and checks whether the resulting number contains between 10 and 15 digits.

### 3. Partial Name Matching

**Challenge:** Users may remember only part of a contact's name.

**Solution:** The program converts search terms and contact names to lowercase and checks whether the search term appears within a name.

### 4. Data Persistence

**Challenge:** Contact information should remain available after the program closes.

**Solution:** The program uses Python's `json` module to save contacts to a file and load them when the program starts.

### 5. Invalid Email Addresses

**Challenge:** Users may enter email addresses in an incorrect format.

**Solution:** A regular expression checks the email format before the contact is saved.

### 6. Accidental Deletion

**Challenge:** Users may accidentally delete a contact.

**Solution:** The program asks for confirmation before deleting a contact.

### 7. File Handling Errors

**Challenge:** A contact file may not exist or may contain invalid JSON.

**Solution:** Exception handling manages missing or invalid files and prevents the program from crashing during file loading.

## Testing

The project includes automated tests for:

- Valid phone numbers
- Invalid phone numbers
- Valid email addresses
- Invalid email addresses
- Partial name searches
- Searches with no matching contacts
- Search by phone number
- Adding a contact
- Updating a contact
- Deleting a contact
- Saving and loading JSON data

Manual testing should also cover duplicate names, empty names, invalid menu choices, CSV export, backup creation, and persistence after restarting the program.



The Contact Management System demonstrates how Python functions, dictionaries, string methods, input validation, file operations, and exception handling can be combined to build a practical application.

This project provides hands-on experience in organizing code, managing structured data, validating user input, testing functions, and preserving information using JSON files.