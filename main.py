import pysftp #Make sure to run "pip install pysftp" in terminal
from getpass import getpass #for making password input protected

address = input("Enter server address: ")
username = input("Username: ")
password = getpass("Password: ")

sftp = pysftp.Connection(address, username=username, password=password)

sftp.close()