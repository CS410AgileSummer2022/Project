from getpass import getpass                 # For making password input protected
from types import NoneType
from features import SFTP

client = SFTP()

def menuLoop(sftp):
    quitLoop = False
    while not quitLoop:
        opt = input("\nWhat do you want to do?\n(login / logoff / mkdir / ls r / ls l / get / get m / mv l / quit)\n")
        match opt:
            case "login":
                address = input("Enter server address: ")
                username = input("Username: ")
                password = getpass("Password: ")
                sftp = client.login(address, username, password)
                client.printRemoteWorkingDirectory(sftp)
            case "logoff":
                sftp.close()
            case "mkdir":
                dirName = input("Please enter a directory name: ")
                client.makeDir(sftp, dirName)
            case "chmod":
                remotePath = input("Specify Remote Path: ")
                client.chmod(sftp, remotePath)
            case "ls r":
                remotePath = input("Specify Remote Path: ")
                client.printRemoteDirectory(sftp, remotePath)
            case "ls l":
                localPath = input("Specify Local Path: ")
                client.printLocalDirectory(localPath)
            case "get":
                path = input("Specify file path: ")
                dest = input("Specify destination path: ")
                client.getFile(sftp, path, dest)
            case "get m":
                path = client.getMultipleList()
                dest = input("Specify destination path: ")
                client.getMultiple(sftp, path, dest)
            case "mv l":
                localPath = input("Specify full path to local file to rename: ")
                client.renameLocalFile(localPath)
            case "quit":
                if sftp is not None: 
                    sftp.close()
                quitLoop = True

def main():
    sftp = NoneType
    menuLoop(sftp)


if __name__ == "__main__":
    main()