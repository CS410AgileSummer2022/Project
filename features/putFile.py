from stat import S_ISDIR, S_ISREG           # Needed for making get_r portable
import os

def putFile(sftp, src, dest):
    src = src.replace('\\', '/')
    dest = dest.replace('\\', '/')
    if (dest == "."):
        dest = sftp.getcwd()
    if (sftp.isdir(dest)) == False:
        print("Dest path does not exist.")
        return

    if os.path.isfile(src):
        dest = dest + "/" + src.split("/")[-1]
        sftp.put(src, dest)
        print("Success!")
    elif(os.path.isdir(src)):
        put_r_portable(sftp, src, dest)
        print("Success!")
    else:
        print("Source path does not exist.")

def putMultiple(sftp, srcs, dest):
    for src in srcs:
        putFile(sftp, src, dest)

# Fixes recursive upload issues for different Operating Systems
def put_r_portable(sftp, localdir, remotedir, preserve_mtime=False):
    for filename in os.listdir(localdir):
        remotedir = remotedir.replace('\\', '/')
        localdir = localdir.replace('\\', '/')

        remote_path = remotedir + "/" + filename
        local_path = localdir + "/" + filename
        file_attr = os.stat(local_path)
        mode = file_attr.st_mode
        if S_ISDIR(mode):
            sftp.mkdir(remote_path)
            put_r_portable(sftp, local_path, remote_path, preserve_mtime)
        elif S_ISREG(mode):
            sftp.put(local_path, remote_path, preserve_mtime=preserve_mtime)