# install pytest to use import
import pytest
import main
from unittest import mock

# Looking into python mock library
sftp = ("11.111.111.1", "testName", "testPassword", None)

# Test printLocalDirectory
def test_printLocalDirectory():
    pass


# Test Rename File on Local Machine
def test_renameLocalFile():
    pass


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


# Test Login
def test_Login():
    pass


# Test getFile
def test_getFile():
    pass


# Test chmod
def test_chmod():
    pass


def test_MultipleList():
    pass


def test_getMultiple():
    pass


# Testing Main
def test_main():
    pass
