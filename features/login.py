import pysftp
from getpass import getpass                 # For making password input protected

def login(address, username, password):
    #username = input("Username: ")
    #password = getpass("Password: ")

    # 'Fixes' known bug with pysftp where no hostkey is found for remote server. 
    # See https://stackoverflow.com/questions/53864260/no-hostkey-for-host-found-when-connecting-to-sftp-server-with-pysftp-usi
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    sftp = pysftp.Connection(address, username=username, password=password, cnopts=cnopts)
    # Set a current working directory directly succeeding connection to remote host (works for linux.cs.pdx.edu)
    sftp.cwd(f"/u/{username}")
    return sftp