import pysftp #Make sure to run "pip install pysftp" in terminal
from getpass import getpass #for making password input protected

def makeDir(stfp, dirName):
    sftp.mkdir(dirName)
    print(dirName + " has been made!")


address = input("Enter server address: ")
username = input("Username: ")
password = getpass("Password: ")

sftp = pysftp.Connection(address, username=username, password=password)
dirName = input("Please enter a directory name: ")
makeDir(sftp, dirName)

sftp.close()