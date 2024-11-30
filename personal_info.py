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