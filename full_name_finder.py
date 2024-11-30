import os

def find_information(fullname, file_name="personal_information.txt"):
    try:
        if not os.path.exists(file_name):
            print("\nNo records found. Please add some information first.")
            return None

        with open(file_name, "r") as file:
            content = file.read()

            if fullname in content:
                records = content.split("-" * 40)  
                for record in records:
                    if fullname in record:
                        return record  
                return None  
            else:
                return None  
    except IOError as e:
        print(f"\nAn error occurred while reading the file: {e}")
        return None
    
def display_person_info(info):
    if info:
        print("\nInformation Found:\n")
        print(info)
    else:
        print("\nNo information found for this person.")

def search_person():
    fullname = input("Enter the full name to search: ").strip()

    info = find_information(fullname)

    display_person_info(info)

def main():
    while True:
        search_person() 
        
        continue_search = input("\nDo you want to search for another person? (yes/no): ").strip().lower()
        if continue_search != "yes":
            print("\nExiting program. Goodbye!")
            break 

if __name__ == "__main__":
    main() 
