import os
from datetime import datetime

def display_menu():
    print("\nOptions:")
    print("1. Add a new person")
    print("2. View records")
    print("3. Exit")
    return input("Enter your choice: ").strip()

def view_records(file_name="personal_information.txt"):
    try:
        if not os.path.exists(file_name):
            print("\nNo records found. Please add some information first.")
            return

        with open(file_name, "r") as file:
            content = file.read()
            if content.strip():
                print("\nCurrent Records:\n")
                print(content)
            else:
                print("\nNo records found in the file.")
    except IOError as e:
        print(f"\nAn error occurred while reading the file: {e}")

def collect_information():
    fullname = input("Full Name: ").strip()
    address = input("Address: ").strip()
    age = input("Age: ").strip()
    contact_number = input("Contact Number: ").strip()
    email = input("Email Address: ").strip()

    additional_info = {}
    while True:
        add_field = input("Do you want to add additional information? (yes/no): ").strip().lower()
        if add_field == "yes":
            key = input("Enter the field name: ").strip()
            value = input(f"Enter the value for {key}: ").strip()
            additional_info[key] = value
        elif add_field == "no":
            break

    
    with open("personal_information.txt", "a") as file:
        file.write(f"Full Name: {fullname}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Contact Number: {contact_number}\n")
        file.write(f"Email Address: {email}\n")
        for key, value in additional_info.items():
            file.write(f"{key}: {value}\n")
        file.write("-" * 40 + "\n")

def main():
    while True:
        choice = display_menu()
        if choice == "1":
            collect_information()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()