import os
def manage_files(directory, create=True, file_name="sample.txt"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path=os.path.join(directory, file_name)
    if create:
        with open(file_path,'w') as f:
            f.write("sample file")
            print(f"{file_path} created succesfully")
    else:
        if (os.path.exists(file_path)):
            os.remove(file_path)
            print(f"{file_path} removed successfully")
        else:
            print(f"{file_path} does not exist")
# manage_files("test_dir", create=True, file_name="test.txt")
# manage_files("test_dir", create=False, file_name="test.txt")

def list_files(directory):
    for file in os.listdir(directory):
        path=os.path.join(directory,file)
        if (os.path.isfile(path)):
            print(f"{os.path.getsize(path)}bytes")
list_files("test_dir")

def list_files(directory):
    for file in os.listdir(directory):
        path=os.path.join(directory)
        if os.path.isfile(path):
            print(f"{os.path.getsize(path)} bytes")