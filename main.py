from types import NoneType
import pysftp                       # Make sure to run "pip install pysftp" in terminal
from getpass import getpass         # for making password input protected
import os                           # Utils for current OS
import re                           # Python regex


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

def login(address, username, password):
    # 'Fixes' known bug with pysftp where no hostkey is found for remote server. 
    # See https://stackoverflow.com/questions/53864260/no-hostkey-for-host-found-when-connecting-to-sftp-server-with-pysftp-usi
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    sftp = pysftp.Connection(address, username=username, password=password, cnopts=cnopts)
    # Set a current working directory directly succeeding connection to remote host (works for linux.cs.pdx.edu)
    sftp.cwd(f"/u/{username}")
    return sftp

# Get file from remote server
def getFile(sftp, path, dest):
    dest = dest.replace('\\', '/')
    if(sftp.isfile(path)):
        #checks if the last character of the destination is a \
        if(dest[-1] != "/"):
            dest = dest+"/"

        #check if the destination exists
        if(os.path.exists(dest) == False):
            print("Destination path does not exist.")
            return

        #appends the file name to the destination path
        dest = dest+path.split("/")[-1]

        #download the file
        sftp.get(path, dest)
        print("Success!")
    else:
        print("Specified path is not a file.")
 
# change the perms on the remote server
def chmod(sftp, path):
    # check if the remote path exists
    if(sftp.lexists(path) == False):
        print("Remote path does not exist!")
        return

    reg = re.compile('[0-7]+')                  # regex to match for octal strings
    mode = input("Please enter octal code: ")   # capture the user input
    match = reg.match(mode)                     # compare the input string to the octal regex
    
    # ensures that the match is consitent across the whole string
    if(match.start() == 0 and match.end() == len(mode)):
        sftp.chmod(path, mode)
        return
    else:
        print("Not a valid octal code!")
        return

def menuLoop(sftp, local):
    quitLoop = False
    while not quitLoop:
        opt = input("\nWhat do you want to do?\n(login / logoff / mkdir / ls r / ls l / get / quit)\n")
        match opt:
            case "login":
                address = input("Enter server address: ")
                username = input("Username: ")
                password = getpass("Password: ")
                sftp = login(address, username, password)
                printRemoteWorkingDirectory(sftp)
            case "logoff":
                sftp.close()
            case "mkdir":
                dirName = input("Please enter a directory name: ")
                makeDir(sftp, dirName)
            case "chmod":
                remotePath = input("Specify Remote Path: ")
                chmod(sftp, remotePath)
            case "ls r":
                remotePath = input("Specify Remote Path: ")
                printRemoteDirectory(sftp, remotePath)
            case "ls l":
                localPath = input("Specify Local Path: ")
                local.printLocalDirectory(localPath)
            case "get":
                path = input("Specify file path: ")
                dest = input("Specify destination path: ")
                getFile(sftp, path, dest)
            case "quit":
                if sftp is not None: 
                    sftp.close()
                quitLoop = True

def main():
    local = Local()
    sftp = NoneType
    menuLoop(sftp, local)


if __name__ == "__main__":
    main()