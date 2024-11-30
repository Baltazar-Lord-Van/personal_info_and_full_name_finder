import os

# Function to check if a record with the same full name already exists in the file.
def is_duplicate(fullname, file_name="personal_information.txt"):
    try:
        # If the file does not exist, return False as there can't be duplicates.
        if not os.path.exists(file_name):
            return False  # File doesn't exist; no duplicates possible.

        # Open the file and check if the fullname exists in the contents.
        with open(file_name, "r") as file:
            content = file.read()
            if fullname in content:
                return True  # Duplicate found.
        return False  # No duplicate found.
    except IOError as e:
        # If an error occurs while reading the file, display an error message.
        print(f"\nAn error occurred while checking for duplicates: {e}")
        return False  # Return False in case of an error.

# Function to display the menu options.
def display_menu():
    print("\nOptions:")
    print("1. Add a new person")  # Option to add a new person's information.
    print("2. View records")  # Option to view the stored records.
    print("3. Exit")  # Option to exit the program.
    return input("Enter your choice: ").strip()  # Return the user's choice.

# Function to view the stored records in the file.
def view_records(file_name="personal_information.txt"):
    try:
        # Check if the file exists, if not, prompt the user to add information.
        if not os.path.exists(file_name):
            print("\nNo records found. Please add some information first.")
            return

        # Open and read the file contents.
        with open(file_name, "r") as file:
            content = file.read()
            if content.strip():
                # If the file is not empty, print the current records.
                print("\nCurrent Records:\n")
                print(content)
            else:
                # If the file is empty, notify the user.
                print("\nNo records found in the file.")
    except IOError as e:
        # If an error occurs while reading the file, display an error message.
        print(f"\nAn error occurred while reading the file: {e}")

# Function to collect and save personal information.
def collect_information():
    # Prompt the user for personal details.
    fullname = input("Full Name: ").strip()

    # Check if the record already exists, if it does, exit the function.
    if is_duplicate(fullname):
        print("\nThis record already exists. Duplicate entry is not allowed.")
        return  # Exit the function if it's a duplicate.

    # Collect additional personal information.
    address = input("Address: ").strip()
    age = input("Age: ").strip()
    contact_number = input("Contact Number: ").strip()
    email = input("Email Address: ").strip()

    # A dictionary to hold additional information the user may wish to provide.
    additional_info = {}
    while True:
        # Ask the user if they want to add more fields.
        add_field = input("Do you want to add additional information? (yes/no): ").strip().lower()
        if add_field == "yes":
            # If yes, ask for the field name and its value.
            key = input("Enter the field name: ").strip()
            value = input(f"Enter the value for {key}: ").strip()
            additional_info[key] = value  # Store the field and value in the dictionary.
        elif add_field == "no":
            break  # Exit the loop if no more fields are to be added.
    
    # Open the file in append mode and save the information.
    with open("personal_information.txt", "a") as file:
        file.write(f"Full Name: {fullname}\n")  # Write the full name.
        file.write(f"Address: {address}\n")  # Write the address.
        file.write(f"Age: {age}\n")  # Write the age.
        file.write(f"Contact Number: {contact_number}\n")  # Write the contact number.
        file.write(f"Email Address: {email}\n")  # Write the email address.
        
        # Write any additional information added by the user.
        for key, value in additional_info.items():
            file.write(f"{key}: {value}\n")
        
        # Separate records with a line of dashes for clarity.
        file.write("-" * 40 + "\n")

# The main function that drives the program.
def main():
    while True:
        # Display the menu and get the user's choice.
        choice = display_menu()

        # Perform actions based on the user's choice.
        if choice == "1":
            collect_information()  # Collect and save information.
        elif choice == "2":
            view_records()  # Display the stored records.
        elif choice == "3":
            print("\nExiting program. Goodbye!")  # Exit the program.
            break  # Break the loop to exit
        else:
            # If the user enters an invalid option, ask them to try again.
            print("\nInvalid choice. Please try again.")

# Entry point of the program, runs the main function if the script is executed directly.
if __name__ == "__main__":
    main()
