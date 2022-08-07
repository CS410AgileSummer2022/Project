import os

# Print contents of a directory on local machine at specified path
def printLocalDirectory(path):
    dir_list = os.listdir(path)
    for item in dir_list:
        print(item)

# Print the contents of a directory on the remote host from the specified path
def printRemoteDirectory(sftp, path):
    dirContents = sftp.listdir()
    for item in dirContents:
        print(item)

# Print the Current Working Directory in the remote host
def printRemoteWorkingDirectory(sftp):
    workingDirectory = sftp.getcwd()
    print(f"cwd: {workingDirectory}")
    return True