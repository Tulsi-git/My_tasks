"""
A simple contact book where users can add, view, update, and delete contacts.

Concepts Used:

✅ OOP (Classes & Objects)
✅ File Handling (CSV or JSON)
✅ Dictionary for Data Storage
"""
import json



class ContactBook():
    def __init__(self):
        self.filename = "contacts.csv"
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file , indent=4)

    def add_contacts(self, name, phone, email):
        self.contacts[name] = {"phone" : phone, "email" : email}
        self.save_contacts()
        print("Contact added")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found")
        else:
            print("\n Contacts list : ")
            for name, details in self.contacts.items():
                print(f"{name} - {details['phone']} | {details['email']}")

    def delete_contacts(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f" {name} removed.")
        else:
            print("Contact not found")

def main():
    book = ContactBook()

    while True:
        print("\n Contact Book")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            name = input("Enter name : ")
            phone = input("Enter phone : ")
            email = input("Enter email : ")
            book.add_contacts(name, phone, email)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            name = input("Enter contact name to delete : ")
            book.delete_contacts(name)
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()




            