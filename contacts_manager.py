
# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
import csv
import os
import shutil
from datetime import datetime, timedelta

FILE_NAME = "contacts_data.json"
BACKUP_FILE = "contacts_backup.json"

# Main dictionary
contacts = {}


# 1. Validate phone number
def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)

    if 10 <= len(digits) <= 15:
        return True, digits

    return False, None


# 2. Validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# 3. Save contacts to JSON file
def save_to_file(contacts):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contacts saved to", FILE_NAME)

    except OSError as e:
        print("Error saving contacts:", e)


# 4. Load contacts from JSON file
def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            if isinstance(data, dict):
                print("Contacts loaded successfully!")
                return data

            print("Invalid contact data. Starting fresh.")
            return {}

    except FileNotFoundError:
        print("No existing contacts file found. Starting fresh.")
        return {}

    except (json.JSONDecodeError, OSError) as e:
        print("Error loading contacts:", e)
        return {}


# 5. Create backup
def backup_contacts():
    if not os.path.exists(FILE_NAME):
        print("No saved contacts available for backup.")
        return

    try:
        shutil.copy2(FILE_NAME, BACKUP_FILE)
        print("Backup created successfully!")

    except OSError as e:
        print("Backup failed:", e)


# 6. Add contact
def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")

    while True:
        name = input("Enter contact name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        if name in contacts:
            print("Contact already exists!")

            choice = input(
                "Do you want to update instead? (y/n): "
            ).strip().lower()

            if choice == "y":
                update_contact(contacts, name)

            return

        break

    while True:
        phone = input("Enter phone number: ").strip()
        valid, cleaned_phone = validate_phone(phone)

        if valid:
            break

        print("Invalid phone number! Enter 10-15 digits.")

    while True:
        email = input(
            "Enter email (optional, press Enter to skip): "
        ).strip()

        if not email or validate_email(email):
            break

        print("Invalid email format!")

    address = input("Enter address (optional): ").strip()

    group = input(
        "Enter group (Friends/Work/Family/Other): "
    ).strip() or "Other"

    now = datetime.now().isoformat()

    contacts[name] = {
        "phone": cleaned_phone,
        "email": email if email else None,
        "address": address if address else None,
        "group": group,
        "created_at": now,
        "updated_at": now
    }

    print("Contact '" + name + "' added successfully!")
    save_to_file(contacts)


# 7. Search contacts by partial name
def search_contacts(contacts, search_term):
    search_term = search_term.strip().lower()
    results = {}

    if not search_term:
        print("Search term cannot be empty!")
        return results

    for name, info in contacts.items():
        if search_term in name.lower():
            results[name] = info

    return results


# 8. Search contacts by phone number
def search_by_phone(contacts, phone):
    digits = re.sub(r'\D', '', phone)
    results = {}

    if not digits:
        print("Please enter a valid search number.")
        return results

    for name, info in contacts.items():
        if digits in info.get("phone", ""):
            results[name] = info

    return results


# 9. Display search results
def display_search_results(results):
    if not results:
        print("No contacts found.")
        return

    print("\nFound", len(results), "contact(s)")
    print("-" * 50)

    for i, (name, info) in enumerate(results.items(), 1):
        print(str(i) + ".", name)
        print("   Phone:", info.get("phone", ""))
        print("   Email:", info.get("email") or "Not provided")
        print("   Address:", info.get("address") or "Not provided")
        print("   Group:", info.get("group", "Other"))
        print("-" * 50)


# 10. Search contact menu
def search_contact(contacts):
    print("\n--- SEARCH CONTACT ---")
    print("1. Search by name")
    print("2. Search by phone number")

    choice = input("Enter choice (1-2): ").strip()

    if choice == "1":
        term = input("Enter name to search: ")
        results = search_contacts(contacts, term)
        display_search_results(results)

    elif choice == "2":
        phone = input("Enter phone number to search: ")
        results = search_by_phone(contacts, phone)
        display_search_results(results)

    else:
        print("Invalid search choice!")


# 11. Update contact
def update_contact(contacts, existing_name=None):
    print("\n--- UPDATE CONTACT ---")

    if existing_name is None:
        name = input("Enter contact name to update: ").strip()
    else:
        name = existing_name

    if name not in contacts:
        print("Contact not found!")
        return

    info = contacts[name]

    print("Press Enter to keep the existing value.")

    new_name = input(
        "New name [" + name + "]: "
    ).strip()

    if new_name and new_name != name:
        if new_name in contacts:
            print("Another contact already uses that name!")
            return

    new_phone = input(
        "New phone [" + info["phone"] + "]: "
    ).strip()

    if new_phone:
        valid, cleaned_phone = validate_phone(new_phone)

        if not valid:
            print("Invalid phone number!")
            return

        info["phone"] = cleaned_phone

    new_email = input(
        "New email [" + (info.get("email") or "") + "]: "
    ).strip()

    if new_email:
        if not validate_email(new_email):
            print("Invalid email format!")
            return

        info["email"] = new_email

    new_address = input(
        "New address [" + (info.get("address") or "") + "]: "
    ).strip()

    if new_address:
        info["address"] = new_address

    new_group = input(
        "New group [" + info.get("group", "Other") + "]: "
    ).strip()

    if new_group:
        info["group"] = new_group

    if new_name and new_name != name:
        contacts[new_name] = contacts.pop(name)

    info["updated_at"] = datetime.now().isoformat()

    print("Contact updated successfully!")
    save_to_file(contacts)


# 12. Delete contact
def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")

    name = input("Enter contact name to delete: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input(
        "Are you sure you want to delete " + name + "? (y/n): "
    ).strip().lower()

    if confirm == "y":
        del contacts[name]
        print("Contact deleted successfully!")
        save_to_file(contacts)
    else:
        print("Deletion cancelled.")


# 13. Display all contacts
def display_all(contacts):
    print("\n--- ALL CONTACTS (" + str(len(contacts)) + " total) ---")
    print("=" * 60)

    if not contacts:
        print("No contacts available.")
        return

    for name, info in sorted(contacts.items()):
        print("Name:", name)
        print("Phone:", info.get("phone", ""))
        print("Email:", info.get("email") or "Not provided")
        print("Address:", info.get("address") or "Not provided")
        print("Group:", info.get("group", "Other"))
        print("-" * 60)


# 14. Export contacts to CSV
def export_to_csv(contacts):
    if not contacts:
        print("No contacts available to export.")
        return

    try:
        with open("contacts_export.csv", "w", newline="",
                  encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Name", "Phone", "Email",
                "Address", "Group", "Created At", "Updated At"
            ])

            for name, info in contacts.items():
                writer.writerow([
                    name,
                    info.get("phone", ""),
                    info.get("email") or "",
                    info.get("address") or "",
                    info.get("group", "Other"),
                    info.get("created_at", ""),
                    info.get("updated_at", "")
                ])

        print("Contacts exported to contacts_export.csv")

    except OSError as e:
        print("CSV export failed:", e)


# 15. Contact statistics
def show_statistics(contacts):
    print("\n--- CONTACT STATISTICS ---")

    total = len(contacts)
    print("Total Contacts:", total)

    if total == 0:
        print("No statistics available yet.")
        return

    groups = {}

    for info in contacts.values():
        group = info.get("group", "Other")
        groups[group] = groups.get(group, 0) + 1

    print("\nContacts by Group:")

    for group, count in sorted(groups.items()):
        print(" ", group + ":", count, "contact(s)")

    cutoff = datetime.now() - timedelta(days=7)
    recent = 0

    for info in contacts.values():
        updated = info.get("updated_at", "")

        try:
            updated_date = datetime.fromisoformat(updated)

            if updated_date >= cutoff:
                recent += 1

        except (ValueError, TypeError):
            pass

    print("\nRecently Updated (last 7 days):", recent)


# 16. Main menu
def main():
    contacts = load_from_file()

    print("\n" + "=" * 50)
    print("       CONTACT MANAGEMENT SYSTEM")
    print("=" * 50)

    while True:
        print("\n==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Create Backup")
        print("9. Exit")
        print("==============================")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            display_all(contacts)

        elif choice == "6":
            export_to_csv(contacts)

        elif choice == "7":
            show_statistics(contacts)

        elif choice == "8":
            backup_contacts()

        elif choice == "9":
            save_to_file(contacts)
            print("\n" + "=" * 50)
            print("Thank you for using Contact Management System!")
            print("=" * 50)
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 9.")


# Start the program
if __name__ == "__main__":
    main()
