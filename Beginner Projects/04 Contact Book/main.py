class ContactBook:
    def __init__(self):
        self.contacts = dict()

    def _check_contact(self, name):
        if name not in self.contacts:
            print("Contact not found!")
            return True
        return False
    
    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact added successfully!")

    def delete_contact(self, name):
        if self._check_contact(name):
            return
        del self.contacts[name]
        print("Contact deleted successfully.")

    def search_contacts(self, name):
        if self._check_contact(name):
            return
        print(f"|Contact info of {name}|\n")
        print(f"Phone: {self.contacts[name]['phone']}")
        print(f"Email: {self.contacts[name]['email']}")
        print(f"Address: {self.contacts[name]['address']}")
        print("-----------------------")

    def view_contacts(self):
        for name, info in self.contacts.items():
            print(f"Name: ", name)
            print(f"Phone: ", info['phone'])
            print(f"Email: ", info['email'])
            print(f"Address: ", info['address'])
            print("-----------------------")

    def update_contact(self, name, phone=None, email=None, address=None):
        if self._check_contact(name):
            return
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        if address:
            self.contacts[name]['address'] = address


if __name__ == '__main__':
    contact_book1 = ContactBook()
    while True:
        print("\n--- Contact Book Application ---")
        print("1. Add contact")
        print("2. Edit contact")
        print("3. View contacts")
        print("4. Search contact")
        print("5. Delete contact")
        print("6. Quit")

        user_choice = input("\nEnter the number of the option you want: ")

        if user_choice == '1':
            name = input("\nEnter contact name: ")
            if name not in contact_book1.contacts:
                phone = input("Enter contact phone: ")
                email = input("Enter contact email: ")
                address = input("Enter contact address: ")
                contact_book1.add_contact(name, phone, email, address)
            else:
                print("Contact already exists in your contacts!")

        elif user_choice == '2':
            name = input("\nEnter the name of contact to edit: ")
            if name in contact_book1.contacts:
                phone = input("Enter the new/updated phone number or press Enter to keep unchange: ")
                email = input("Enter the new/updated email or press Enter to keep unchange: ")
                address = input("Enter the new/updated address or press Enter to keep unchange: ")
                contact_book1.update_contact(name, phone or None, email or None, address or None)
            if name not in contact_book1.contacts:
                print("Contact not found!")

        elif user_choice == '3':
            print("\nList of contacts:")
            contact_book1.view_contacts()
        
        elif user_choice == '4':
            name = input("\nEnter the contact name: ")
            contact_book1.search_contacts(name)

        elif user_choice == '5':
            name = input("\nEnter the contact name: ")
            contact_book1.delete_contact(name)
        
        elif user_choice == '6':
            print("\nThank you for using Contact Book app see you again!")
            break

        else:
            print("\nInvalid input! Try again.")
