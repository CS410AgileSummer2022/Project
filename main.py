import pysftp #Make sure to run "pip install pysftp" in terminal
from getpass import getpass #for making password input protected
import os


class Local:
    def printLocalDirectory(self, path):
        dir_list = os.listdir(path)
        for item in dir_list:
            print(item)


def makeDir(sftp, dirName):
    sftp.mkdir(dirName)
    print(dirName + " has been made!")


# Print the Current Working Directory in the remote host
def printRemoteWorkingDirectory(sftp):
    workingDirectory = sftp.getcwd()
    print(f"cwd: {workingDirectory}")


# Print the contents of a directory on the remote host from the specified path
def printRemoteDirectory(sftp, path):
    dirContents = sftp.listdir()
    for item in dirContents:
        print(item)


def main():
    local = Local()
    localPath = input("Specify Local Path: ")
    local.printLocalDirectory(localPath)

    address = input("Enter server address: ")
    username = input("Username: ")
    password = getpass("Password: ")

    # 'Fixes' known bug with pysftp where no hostkey is found for remote server. 
    # See https://stackoverflow.com/questions/53864260/no-hostkey-for-host-found-when-connecting-to-sftp-server-with-pysftp-usi
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    sftp = pysftp.Connection(address, username=username, password=password, cnopts=cnopts)
    
    # Set a current working directory directly succeeding connection to remote host (works for linux.cs.pdx.edu)
    sftp.cwd(f"/u/{username}")

    printRemoteWorkingDirectory(sftp)

    remotePath = input("Specify Remote Path: ")
    printRemoteDirectory(sftp, remotePath)

    dirName = input("Please enter a directory name: ")
    makeDir(sftp, dirName)

    sftp.close()


if __name__ == "__main__":
    main()