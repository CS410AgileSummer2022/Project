def makeDir(sftp, dirName):
    sftp.mkdir(dirName)
    print(dirName + " has been made!")