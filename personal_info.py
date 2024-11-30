def display_menu():
    print("\nOptions:")
    print("1. Add a new person")
    print("2. Exit")
    return input("Enter your choice: ").strip()

def collect_information():
    fullname = input("Full Name: ").strip()
    address = input("Address: ").strip()
    age = input("Age: ").strip()
    contact_number = input("Contact Number: ").strip()
    email = input("Email Address: ").strip()

    with open("personal_information.txt", "a") as file:
        file.write(f"Full Name: {fullname}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Contact Number: {contact_number}\n")
        file.write(f"Email Address: {email}\n")
        file.write("-" * 40 + "\n")

def main():
    while True:
        choice = display_menu()
        if choice == "1":
            collect_information()  
        elif choice == "2":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()