import os
import hashlib

# 1. Automate file creation and deletion in a specified directory


def manage_files(directory, create=True, file_name="example.txt"):
    # Ensure the directory exists before creating or deleting the file
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, file_name)

    if create:
        with open(file_path, 'w') as f:
            f.write("Sample text file.")
        print(f"File '{file_path}' created successfully.")
    else:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")

# Call the function to test
manage_files("test_dir", create=True, file_name="test.txt")  # Creates the file
# manage_files("test_dir", create=False, file_name="test.txt") # Deletes the file


#  2. List all files in a directory and display their sizes
def list_files(directory):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            print(f"{file}: {os.path.getsize(path)} bytes")
# list_files("test_dir")

# 5. Secure passwords using hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example: Calling the function
hashed_pw = hash_password("securepassword123")
print("Hashed Password:", hashed_pw)

