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