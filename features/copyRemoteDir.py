import io

def copyRemoteDir(sftp, source, destination):
    if not sftp.exists(source) or not sftp.exists(destination):
        print("One of the specified paths does not exists.")
        return

    if not sftp.isdir(source):
        print("Source path is not a directory.")
        return

    if not sftp.isdir(destination):
        print("Destination path is not a directory.")
        return

    sourceDirs = source.split("/")
    dirName = sourceDirs.pop()
    destinationDirs = destination.split("/")

    if sourceDirs == destinationDirs:
        dirName += "_copy"

    newDir = destination + "/" + dirName
    sftp.mkdir(newDir)
    copyDir_r(sftp, source, newDir)

# Recursively copies a remote directory
def copyDir_r(sftp, source, newDir):
    for entry in sftp.listdir(source):
        sourceSubPath = source + "/" + entry
        newDirSubPath = newDir + "/" + entry

        if sftp.isdir(sourceSubPath):
            sftp.mkdir(newDirSubPath)
            copyDir_r(sftp, sourceSubPath, newDirSubPath)

        elif sftp.isfile(sourceSubPath):
            flo = io.BytesIO()
            sftp.getfo(sourceSubPath, flo)
            flo.seek(0)
            sftp.putfo(flo, newDirSubPath)
