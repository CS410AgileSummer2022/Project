from importlib.resources import path
from types import NoneType
import pysftp                               # Make sure to run "pip install pysftp" in terminal
from getpass import getpass                 # For making password input protected
import os                                   # Utils for native OS
from stat import S_ISDIR, S_ISREG           # Needed for making get_r portable
import re                                   # Python Regex

# Print contents of a directory on local machine at specified path
def printLocalDirectory(path):
    dir_list = os.listdir(path)
    for item in dir_list:
        print(item)

# Rename a file on local machine using full path to file and a new file name 
def renameLocalFile(path_to_file):
    old_file_name = os.path.basename(path_to_file)
    new_file_name = input("New file name: ")
    path_to_dir = os.path.dirname(path_to_file)
    os.rename(f"{path_to_file}", f"{path_to_dir}/{new_file_name}")
    print(f"{old_file_name} has been successfully renamed to {new_file_name} in the local directory {path_to_dir}")

#Rename a file in the remote directory.
def renameRemoteFile(sftp, path_to_file):
    workingDirectory = sftp.getcwd()



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
    #check if the destination exists
    if(os.path.exists(dest) == False):
        print("Destination path does not exist.")
        return

    #checks if the last character of the destination is a /
    if(dest[-1] != "/"):
        dest = dest+"/"

    # if the path is a file, then only download one thing
    if(sftp.isfile(path)):
        #appends the file name to the destination path
        dest = dest+path.split("/")[-1]

        #download the file
        sftp.get(path, dest)
        print("Success!")

    # if the path is a dir, then copy the whole dir
    elif(sftp.isdir(path)):
        get_r_portable(sftp, path, dest)
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

# Fixes recursive download issues for different Operating Systems
def get_r_portable(sftp, remotedir, localdir, preserve_mtime=False):
    for entry in sftp.listdir_attr(remotedir):
        remotepath = remotedir + "/" + entry.filename
        localpath = os.path.join(localdir, entry.filename)
        mode = entry.st_mode
        if S_ISDIR(mode):
            try:
                os.mkdir(localpath)
            except OSError:     
                pass
            get_r_portable(sftp, remotepath, localpath, preserve_mtime)
        elif S_ISREG(mode):
            sftp.get(remotepath, localpath, preserve_mtime=preserve_mtime)

def getMultipleList():
    pathNames = input("Enter file names seperated by a space: ")
    pathNames = pathNames.split(" ")
    return pathNames

def getMultiple(sftp, paths, dest):
    for path in paths:
        getFile(sftp, path, dest)

def menuLoop(sftp):
    quitLoop = False
    while not quitLoop:
        opt = input("\nWhat do you want to do?\n(login / logoff / mkdir / ls r / ls l / get / get m / mv l / quit)\n")
        match opt:
            case "login":
                address = input("Enter server address: ")
                username = input("Username: ")
                password = getpass("Password: ")
                sftp = login(address, username, password)
                printRemoteWorkingDirectory(sftp)
            case "mv r":
                remotePath = input("Specify full path to remote file to rename: ")
                renameRemoteFile(sftp, remotePath)
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
                printLocalDirectory(localPath)
            case "get":
                path = input("Specify file path: ")
                dest = input("Specify destination path: ")
                getFile(sftp, path, dest)
            case "get m":
                path = getMultipleList()
                dest = input("Specify destination path: ")
                getMultiple(sftp, path, dest)
            case "mv l":
                localPath = input("Specify full path to local file to rename: ")
                renameLocalFile(localPath)
            case "quit":
                if sftp is not None: 
                    sftp.close()
                quitLoop = True
def main():
    sftp = NoneType
    menuLoop(sftp)


if __name__ == "__main__":
    main()