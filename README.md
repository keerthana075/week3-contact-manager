# Contact Management System

## 1. Project Description

The **Contact Management System** is a Python-based application that allows users to store, manage, search, update, and delete contact information.

This project uses Python dictionaries, functions, input validation, and JSON file handling to provide a simple and organized way to manage contacts. It also supports exporting contact information to CSV, viewing statistics, and creating backups.

This project was developed as a beginner-friendly Python project to practice programming concepts through a real-world application.

## 2. Project Objectives

- To store contact information using Python dictionaries.
- To create separate functions for contact operations.
- To implement Create, Read, Update, and Delete (CRUD) operations.
- To validate names, phone numbers, and email addresses.
- To save and load contact information using JSON files.
- To search contacts using partial name or phone number matching.
- To export contact information to CSV.
- To practice exception handling and file operations.
- To maintain project documentation and use GitHub for version control.

## 3. Technologies Used

- **Programming Language:** Python
- **Data Structure:** Dictionaries
- **Data Storage:** JSON
- **Data Export:** CSV
- **Testing:** Python `unittest` module
- **Version Control:** Git and GitHub

## 4. Features

- Add new contacts with input validation.
- Search contacts using partial name or phone number.
- Update existing contact information.
- Delete contacts with confirmation.
- Display all saved contacts in a formatted layout.
- Save contact data to a JSON file.
- Load contact data when the program starts.
- Export contact information to a CSV file.
- View contact statistics and group counts.
- Validate phone numbers and email addresses.
- Create a backup of contact information.
- Handle invalid inputs and file-related errors.
- Provide a menu-driven user interface.

## 5. Project Structure

```text
week3-contact-manager/
│
├── contacts_manager.py
├── test_contacts.py
├── contacts_data.json
├── requirements.txt
├── README.md
└── .gitignore
```

### File Explanation

- **contacts_manager.py:** Contains the main application, menu, validation functions, and contact management operations.
- **test_contacts.py:** Contains unit tests to check important functions and application operations.
- **contacts_data.json:** Stores contact information in JSON format. It may be created or updated when the application runs.
- **requirements.txt:** Lists any external Python packages required by the project.
- **README.md:** Contains project documentation and instructions.
- **.gitignore:** Specifies files that Git should not track.

## 6. Data Structure

The project uses a nested Python dictionary to store contact information.

Example:

```python
contacts = {
    "John Doe": {
        "phone": "+1234567890",
        "email": "john@example.com",
        "address": "123 Main Street",
        "group": "Friends"
    },
    "Jane Smith": {
        "phone": "+0987654321",
        "email": "jane@example.com",
        "address": "456 Oak Avenue",
        "group": "Work"
    }
}
```

The outer dictionary uses contact names as keys. Each name is associated with another dictionary containing the phone number, email address, address, and group.

This structure makes it easy to retrieve and update contact details.

*Note: These are sample contacts for documentation, not actual user records.*

## 7. Setup and Installation

### Prerequisites

- Python 3 installed on your computer.
- Git installed if you want to upload the project to GitHub.

### Step 1: Open the Project Folder

Open Command Prompt or a terminal and navigate to the project directory.

```bash
cd week3-contact-manager
```

### Step 2: Install Requirements

Run the following command if your project requires additional packages:

```bash
pip install -r requirements.txt
```

If the file contains no external dependencies, no additional packages may be necessary.

### Step 3: Run the Application

```bash
python contacts_manager.py
```

### Step 4: Run the Unit Tests

```bash
python -m unittest -v test_contacts.py
```

The test command displays the results of the tests and helps verify that important operations work correctly.

## 8. Sample Menu

```text
===========================================
       CONTACT MANAGEMENT SYSTEM
===========================================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Create Backup
9. Exit

Enter your choice (1-9):
```

## 9. Sample Output

The following is an illustrative example of searching for a contact.

```text
Search Results for 'john':
------------------------------------------
Name: John Doe
Phone: +1234567890
Email: john@example.com
Address: 123 Main Street
Group: Friends
------------------------------------------
Found 1 contact matching 'john'.
```

The following is an illustrative example of contact statistics.

```text
Contact Statistics
------------------
Total Contacts: 15
Friends: 5 contacts
Work: 7 contacts
Family: 3 contacts
```

Actual output depends on the contact information stored in the application.

## 10. Technical Requirements and Implementation

### 10.1 Dictionaries

Dictionaries store contact names and their corresponding details. This makes contact information organized and accessible through keys.

### 10.2 Separate Functions

Separate functions organize the program into reusable sections. Operations such as adding, searching, updating, and deleting contacts can be handled independently.

### 10.3 Input Validation

Validation functions check user-provided information before it is accepted.

- Phone validation checks whether the phone number follows the supported format.
- Email validation checks whether the email address follows the expected format.
- Name handling helps identify and retrieve the correct contact.

### 10.4 CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

- **Create:** Add a new contact.
- **Read:** Search for contacts and display saved information.
- **Update:** Modify existing contact details.
- **Delete:** Remove a contact from the collection.

### 10.5 JSON File Handling

The Python `json` module allows contact information to be saved to a file and loaded when the program starts. This helps preserve data between program executions.

### 10.6 CSV Export

The application provides an option to export contact details into CSV format, which can be opened using spreadsheet applications.

### 10.7 Error Handling

Exception handling helps the program respond to unexpected situations, such as invalid input or file-related errors.

### 10.8 Unit Testing

The `unittest` module is used to test important functions, including validation, searching, contact operations, and file handling.

## 11. Screenshots of the Working Application

Add screenshots of your actual application here to demonstrate that the program works.

Recommended screenshots:

1. **Main Menu:** Shows the available operations.
2. **Add Contact:** Shows a contact being added successfully.
3. **Search Contact:** Shows search results.
4. **Update and Delete:** Demonstrates modifying or removing a contact.
5. **View All Contacts:** Displays saved contacts.
6. **Statistics:** Shows contact counts.
7. **CSV Export or Backup:** Demonstrates file export or backup creation.
8. **Unit Tests:** Shows the output after running the test command.

Insert each screenshot below its heading in the GitHub README editor. Use real screenshots from your application rather than illustrative examples.

## 12. Challenges and Solutions

### Challenge 1: Validating Phone Numbers

**Solution:** Created a phone validation function to check the supported phone number format and normalize the accepted number.

### Challenge 2: Searching with Partial Matches

**Solution:** Used string methods such as `lower()` to support case-insensitive searching and partial matches.

### Challenge 3: Saving and Loading Data

**Solution:** Used JSON file operations to save contact information and load it again when required.

### Challenge 4: Handling Invalid Input

**Solution:** Used validation and exception handling to reduce errors caused by invalid user input.

### Challenge 5: Exporting Contact Information

**Solution:** Added CSV export functionality so contact details can be used in spreadsheet applications.

## 13. What I Learned

Through this project, I learned:

1. **Functions:** How to create reusable and organized code.
2. **Dictionaries:** How to store and retrieve information using key-value pairs.
3. **String Methods:** How to manipulate text and perform case-insensitive searches.
4. **File Operations:** How to save and load information using JSON.
5. **Input Validation:** How to check user input before processing it.
6. **Error Handling:** How to handle unexpected situations.
7. **CSV Handling:** How to export structured information.
8. **Unit Testing:** How to test functions and identify errors.
9. **Git and GitHub:** How to track code changes and share a project repository.

## 14. Future Improvements

- Add a graphical user interface.
- Implement contact sorting and filtering.
- Add stronger duplicate-contact handling.
- Improve data privacy and access control.
- Add more automated tests.
- Add contact import functionality.

## 15. Conclusion

The Contact Management System demonstrates how Python can be used to build a practical application using dictionaries, functions, validation, file handling, and testing.

This project helped me strengthen my Python fundamentals and understand how to organize a complete beginner-level application. It also provided practical experience with documentation and version control using GitHub.

---

**Project Name:** Contact Management System  
**Language:** Python  
**Repository:** `week3-contact-manager`