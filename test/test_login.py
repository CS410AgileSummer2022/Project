import unittest
from features import SFTP
from unittest.mock import patch

# This is an integration test
class UnitTests(unittest.TestCase):
    client = SFTP()
    sftp = client.login("linux.cs.pdx.edu")

    def test_login(self):
        # self.sftp = self.client.login("linux.cs.pdx.edu")
        cwd = self.client.printRemoteWorkingDirectory(self.sftp)
        self.assertTrue(cwd)
