from stat import S_ISDIR, S_ISREG           # Needed for making get_r portable
import os

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


def getMultiple(sftp, paths, dest):
    for path in paths:
        getFile(sftp, path, dest)

def getMultipleList():
    pathNames = input("Enter file names seperated by a space: ")
    pathNames = pathNames.split(" ")
    return pathNames

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