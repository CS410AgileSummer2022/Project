import os

# Rename a file on local machine using full path to file and a new file name 
def renameLocalFile(path_to_file, new_file_name):
    old_file_name = os.path.basename(path_to_file)
    #new_file_name = input("New file name: ")
    path_to_dir = os.path.dirname(path_to_file)
    os.rename(f"{path_to_file}", f"{path_to_dir}\\{new_file_name}")
    print(f"{old_file_name} has been successfully renamed to {new_file_name} in the local directory {path_to_dir}")

def renameRemoteFile(sftp, path_to_file):
    #Get only the name of the file.
    old_file_name = os.path.basename(path_to_file)
    #Get the directory without the file name.
    path_to_dir = os.path.dirname(path_to_file)
    #Check if the file exists.
    if sftp.isfile(old_file_name):
        #User input a new filename.
        new_file_name = input("New remote file name: ")
        sftp.rename(f"{path_to_dir}/{old_file_name}", f"{path_to_dir}/{new_file_name}")
        print(f"{old_file_name} has been successfully renamed to {new_file_name} in the remote directory {path_to_dir}")
    else:
        print("\nNo such file exists in that remote directory.")