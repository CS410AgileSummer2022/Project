import unittest
from features import SFTP
from unittest.mock import patch

class UnitTests(unittest.TestCase):
    client = SFTP()
    sftp = client.login("linux.cs.pdx.edu")
    
    def test_login(self):
        #self.sftp = self.client.login("linux.cs.pdx.edu")
        cwd = self.client.printRemoteWorkingDirectory(self.sftp)
        self.assertTrue(cwd)

    #needs put and delete to tested easily
    def test_getFile(self):
        #print(self.sftp)
        pass

    #needs put and delete to tested easily
    def test_getMultiple(self):
        pass
    
    def test_makeDir(self):
        pass

    def test_rename(self):
        pass

    def test_printDir(self):
        pass

    def test_chmod(self):
        pass
