import unittest
from features import SFTP
from unittest.mock import patch


class UnitTests(unittest.TestCase):
    client = SFTP()
    sftp = client.login("linux.cs.pdx.edu")

    def test_chmod(self):
        pass
