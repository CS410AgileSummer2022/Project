class SFTP():

    from .login import login
    from .chmod import chmod
    from .getFile import getFile, getMultiple, getMultipleList
    from .putFile import putFile, putMultiple
    from .makeDir import makeDir
    from .printDir import printLocalDirectory, printRemoteDirectory, printRemoteWorkingDirectory
    from .rename import renameLocalFile, renameRemoteFile
    from .copyRemoteDir import copyRemoteDir
    from .DeleteDir import DeleteDir

    login = staticmethod(login)
    chmod = staticmethod(chmod)
    getFile = staticmethod(getFile)
    getMultiple = staticmethod(getMultiple)
    getMultipleList = staticmethod(getMultipleList)
    putFile = staticmethod(putFile)
    putMultiple = staticmethod(putMultiple)
    makeDir = staticmethod(makeDir)
    printLocalDirectory = staticmethod(printLocalDirectory)
    printRemoteDirectory = staticmethod(printRemoteDirectory)
    printRemoteWorkingDirectory = staticmethod(printRemoteWorkingDirectory)
    renameLocalFile = staticmethod(renameLocalFile)
    renameRemoteFile = staticmethod(renameRemoteFile)
    copyRemoteDir = staticmethod(copyRemoteDir)
    DeleteDir = staticmethod(DeleteDir)
