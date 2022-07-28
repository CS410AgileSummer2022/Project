import os

# Rename a file on local machine using full path to file and a new file name 
def renameLocalFile(path_to_file, new_file_name):
    old_file_name = os.path.basename(path_to_file)
    #new_file_name = input("New file name: ")
    path_to_dir = os.path.dirname(path_to_file)
    os.rename(f"{path_to_file}", f"{path_to_dir}\\{new_file_name}")
    print(f"{old_file_name} has been successfully renamed to {new_file_name} in the local directory {path_to_dir}")