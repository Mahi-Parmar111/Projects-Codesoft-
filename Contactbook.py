contact_book = {}

def display_menu():
   
    print("         📱 SMART CONTACT BOOK         ")
  
    print("1. ➕ Add New Contact")
    print("2. 📋 View Contact List")
    print("3. 🔍 Search Contact")
    print("4. 📝 Update Contact")
    print("5. ❌ Delete Contact")
    print("6. 🚪 Exit Application")

   
def add_contact():
    print("\n    Add New Contact  ")
    name = input("Contact name: ").strip().title()
    
    if not name:
        print("⚠️ Name can't be empty!")
        return

    if name in contact_book:
        print(f"⚠️ A contact named '{name}' already exists.")
        return

    phone = input("Phone number: ").strip()
    email = input("Email address: ").strip()
    address = input("Physical address: ").strip()

   
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("\n   Saved Contact List    ")
    if not contact_book:
        print(" Your contact book is currently empty.")
        return

    
    print(f"{'Name':<20} | {'Phone Number':<15}")
   
    
    for name, details in contact_book.items():
        print(f"{name:<20} | {details['phone']:<15}")

def search_contact():
    print("\n    Search Contacts    ")
    if not contact_book:
        print(" No contacts available to search.")
        return

    query = input("Enter Name or Phone Number to search: ").strip().lower()
    found = False

    print(f"\nSearch results for '{query}':")
    print("-" * 50)

    for name, details in contact_book.items():
        
        if query in name.lower() or query in details['phone']:
            print(f"👤 Name:    {name}")
            print(f"📞 Phone:   {details['phone']}")
            print(f"📧 Email:   {details['email']}")
            print(f"🏠 Address: {details['address']}")
            print("-" * 50)
            found = True

    if not found:
        print("❌ No matching contacts found.")

def update_contact():
    print("\n    Update Existing Contact    ")
    name = input("Enter the EXACT name of the contact to update: ").strip().title()

    if name not in contact_book:
        print(f"❌ Contact '{name}' not found.")
        return

    print(f"\nModifying details for {name}. Leave blank to keep current value.")
    
    current_phone = contact_book[name]['phone']
    current_email = contact_book[name]['email']
    current_address = contact_book[name]['address']

    new_phone = input(f"New Phone [{current_phone}]: ").strip()
    new_email = input(f"New Email [{current_email}]: ").strip()
    new_address = input(f"New Address [{current_address}]: ").strip()

    
    if new_phone:   contact_book[name]['phone'] = new_phone
    if new_email:   contact_book[name]['email'] = new_email
    if new_address: contact_book[name]['address'] = new_address

    print(f"🔄 Success: Contact '{name}' updated successfully!")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the EXACT name of the contact to delete: ").strip().title()

    if name in contact_book:
       
        del contact_book[name]
        print(f"🗑️ Success: Contact '{name}' has been permanently deleted.")
    else:
        print(f"❌ Contact '{name}' not found.")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\n👋 Thank you for using Smart Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid Selection! Please type a number between 1 and 6.")


if __name__ == "__main__":
    main()
