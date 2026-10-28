
import unittest
import contacts_manager as cm
import tempfile
import os
import csv
import json
from unittest.mock import patch


class TestContactsManager(unittest.TestCase):

    def setUp(self):
        self.contacts = {
            "John Doe": {
                "phone": "9876543210",
                "email": "john@example.com",
                "address": "Hyderabad",
                "group": "Friends"
            },
            "Priya": {
                "phone": "9876543211",
                "email": "priya@example.com",
                "address": "Vijayawada",
                "group": "Family"
            }
        }

    # Test phone validation
    def test_valid_phone(self):
        result, phone = cm.validate_phone("9876543210")
        self.assertTrue(result)
        self.assertEqual(phone, "9876543210")

    def test_invalid_phone(self):
        result, phone = cm.validate_phone("123")
        self.assertFalse(result)
        self.assertIsNone(phone)

    # Test email validation
    def test_valid_email(self):
        self.assertTrue(cm.validate_email("john@example.com"))

    def test_invalid_email(self):
        self.assertFalse(cm.validate_email("invalid-email"))

    # Test searching contacts
    def test_partial_name_search(self):
        result = cm.search_contacts(self.contacts, "John")
        self.assertIn("John Doe", result)

    def test_search_without_match(self):
        result = cm.search_contacts(self.contacts, "Unknown")
        self.assertEqual(result, {})

    def test_search_by_phone(self):
        result = cm.search_by_phone(self.contacts, "9876543210")
        self.assertIn("John Doe", result)

    # Test adding a contact
    def test_add_contact(self):
        user_inputs = [
            "Anu",
            "9876543212",
            "anu@example.com",
            "Chennai",
            "Friends"
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch.object(cm, "save_to_file"):
                cm.add_contact(self.contacts)

        self.assertIn("Anu", self.contacts)
        self.assertEqual(
            self.contacts["Anu"]["phone"],
            "9876543212"
        )

    # Test updating a contact
    def test_update_contact(self):
        user_inputs = [
            "",             # Keep existing name
            "",             # Keep existing phone
            "",             # Keep existing email
            "New Address",  # Change address
            ""              # Keep existing group
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch.object(cm, "save_to_file"):
                cm.update_contact(self.contacts, "John Doe")

        self.assertEqual(
            self.contacts["John Doe"]["address"],
            "New Address"
        )

    # Test deleting a contact
    def test_delete_contact(self):
        contacts = {
            "John Doe": {
                "phone": "9876543210",
                "email": "john@example.com",
                "address": "Hyderabad",
                "group": "Friends"
            }
        }

        # Change "y" if your function expects a different confirmation.
        user_inputs = ["John Doe", "y"]

        with patch("builtins.input", side_effect=user_inputs):
            with patch.object(cm, "save_to_file"):
                cm.delete_contact(contacts)

        self.assertNotIn("John Doe", contacts)

    # Test saving and loading JSON
    def test_save_and_load_contacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(
                temp_dir, "contacts_data.json"
            )

            with patch.object(cm, "FILE_NAME", file_path):
                cm.save_to_file(self.contacts)
                loaded_contacts = cm.load_from_file()

            self.assertEqual(loaded_contacts, self.contacts)

    # Test exporting contacts to CSV
    
    # Test exporting contacts to CSV
    def test_export_to_csv(self):
        contacts = {
            "John Doe": {
                "phone": "9876543210",
                "email": "john@example.com",
                "address": "Hyderabad",
                "group": "Friends"
            }
        }

        original_directory = os.getcwd()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                os.chdir(temp_dir)

                with patch("builtins.print"):
                    cm.export_to_csv(contacts)

                csv_path = os.path.join(
                    temp_dir, "contacts_export.csv"
                )

                self.assertTrue(os.path.exists(csv_path))

                # Open and close the CSV file safely
                with open(
                    csv_path, "r", newline="", encoding="utf-8"
                ) as file:
                    rows = list(csv.reader(file))

                self.assertGreater(len(rows), 1)
                self.assertIn("John Doe", str(rows))

            finally:
                os.chdir(original_directory)
                
if __name__ == "__main__":
    unittest.main()
