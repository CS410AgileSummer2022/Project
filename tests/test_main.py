# install pytest to use import
import pytest
import main
from unittest import mock

# Looking into python mock library
sftp = ("11.111.111.1", "testName", "testPassword", None)

# Testing make Directory from main.
def test_makeDir():
    pass


# Testing print Remote Working Directory
@mock.patch("getcwd", mock.MagicMock(return_value="/u/testDirectory"))
def test_printRemoteWorkingDirectory():
    assert main.printRemoteWorkingDirectory(sftp)


# Testing Print Remote Directory
def test_printRemoteDirectory():
    pass


# Testing Main
def test_main():
    pass
