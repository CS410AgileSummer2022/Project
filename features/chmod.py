import re

# change the perms on the remote server
def chmod(sftp, path, mode):
    # check if the remote path exists
    if(sftp.lexists(path) == False):
        print("Remote path does not exist!")
        return

    reg = re.compile('[0-7]+')                  # regex to match for octal strings
    match = reg.match(mode)                     # compare the input string to the octal regex
    
    # ensures that the match is consitent across the whole string
    if(match.start() == 0 and match.end() == len(mode)):
        sftp.chmod(path, mode)
        return
    else:
        print("Not a valid octal code!")
        return