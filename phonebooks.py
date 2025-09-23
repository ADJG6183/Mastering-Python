import time 

dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555",
    "Greg": "111-222-3333",
    "Jake": "444-555-6666"
}

def add_contact():
    entries = int(input("How many entries do you want to add? "))
    for i in range(entries):
        key_input = input("Enter the key: ")
        value_input = input("Enter the value: ")
        dict[key_input] = value_input

    print("Contact(s) added successfully.")
    time.sleep(1)
    

def print_contacts():
    if not dict: 
        print("No contacts. please add contacts.")
    else:
        for key, value in dict.items():
            print(f"{key}: {value}")
            time.sleep(1)

def delete_contact():
    number_to_delete = input("Enter the name of the contact to delete: ")
    if number_to_delete in dict:
        del dict[number_to_delete]
        print(f"Contact '{number_to_delete}' deleted successfully.")
    else: 
        print(f"Contact '{number_to_delete}' not found.")
    time.sleep(1)


if __name__ == "__main__":
    print("" \
    "WELOME TO MY PHONEBOOK. YOU ARE HELPING MASTER PYTHON!!!!\n" \
    "Choose an option from those you see here:\n" \
    "########################################\n" \
    "1. Add Contacts\n" \
    "2. Delete a Contact\n" \
    "3. List Contacts\n" \
    "4. Quit\n" \
    "")
    time.sleep(1)
while ans := True:
    ans = input("What would you like to do? ")
    if ans == "1":
        add_contact()
    elif ans == "2":
        delete_contact()
    elif ans == "3":    
        print_contacts()
    elif ans == "4":
        print("\n Goodbye")
        quit()
    elif ans != "":
        print("\n Not Valid Choice Try again")