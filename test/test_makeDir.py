import unittest
from features import SFTP
from unittest.mock import Mock
import sys

sys.path.append("../features")

# def makeDir(sftp, dirName):
#    sftp.mkdir(dirName)
#    print(dirName + " has been made!")


class UnitTests(unittest.TestCase):
    # Creates Fake mock object of SFTP

    def test_makeDir(self):
        client = SFTP()
        # Is a fake return of connection
        sftp = Mock()
        sftp.makeDir("foobar")
        # calling the real code and passing in MOCK "Sftp" and real string
        client.makeDir(sftp, "foobar")
        # confirming that the mock object on client was called correctly
        sftp.mkdir.assert_called_with("foobar")
