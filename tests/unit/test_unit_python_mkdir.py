"""
Module with unit tests for the python_mkdir function.
"""
import os
import sys

from pymkdir.main import python_mkdir
from pymkdir.mkdir import pymkdir

# py2.7 compatibility
if sys.version_info >= (3, 3):
    from unittest import mock
else:
    import mock


@mock.patch("os.access")
@mock.patch("pymkdir.main.pymkdir")
@mock.patch("pymkdir.main.get_command_line_args")
def test_python_mkdir_no_os_access(mocked_get_command_line_args, mocked_pymkdir, mocked_os_access):
    """
    Unit: asserts that pymkdir is not called when os access is restricted.
    """
    # mock responses
    mocked_get_command_line_args.return_value = {"folder": "test_folder", "path": "./mocked_path"}
    mocked_os_access.return_value = False

    # method invocation
    python_mkdir()

    # mock invocation assertions
    mocked_os_access.assert_called_once_with("./mocked_path", os.W_OK)
    mocked_pymkdir.assert_not_called()


@mock.patch("os.access")
@mock.patch("pymkdir.main.pymkdir")
@mock.patch("pymkdir.main.get_command_line_args")
def test_python_mkdir_with_os_access_no_path_exists(
    mocked_get_command_line_args, mocked_pymkdir, mocked_os_access
):
    """
    Unit: asserts that pymkdir is called when os access is not restricted.
    """
    # mock responses
    cls_dict = {"folder": "test_folder", "path": "./mocked_path"}

    mocked_get_command_line_args.return_value = cls_dict
    mocked_os_access.return_value = True  # no OS restriction

    # method invocation
    python_mkdir()

    # mock invocation assertions
    mocked_os_access.assert_called_once_with("./mocked_path", os.W_OK)
    mocked_pymkdir.assert_called_once_with("./mocked_path/test_folder", cls_dict)


@mock.patch("os.mkdir")
@mock.patch("os.path.exists")
def test_mkdir_with_no_os_access(mocked_os_path_exists, mocked_os_mkdir):
    """
    Unit: asserts that os mkdir is not called when the folder name already exists
    """
    cls_dict = {"folder": "test_folder", "path": "./mocked_path"}
    mocked_os_path_exists.return_value = True

    # method invocation
    pymkdir("./mocked_path/test_folder", cls_dict)

    # mock assertions
    mocked_os_path_exists.assert_called_once_with("./mocked_path/test_folder")
    mocked_os_mkdir.assert_not_called()


# 3.x test
if sys.version_info >= (3, 0):

    @mock.patch("builtins.open")
    @mock.patch("os.mkdir")
    @mock.patch("os.path.exists")
    def test_mkdir_with_os_access(mocked_os_path_exists, mocked_os_mkdir, mocked_open):
        """
        Unit: asserts that os mkdir is called when the folder does not exist.
        """
        cls_dict = {"folder": "test_folder", "path": "./mocked_path"}
        mocked_os_path_exists.return_value = False
        mocked_file = mock.Mock()
        mocked_open.return_value = mocked_file

        # method invocation
        pymkdir("./mocked_path/test_folder", cls_dict)

        # mock assertions
        mocked_os_path_exists.assert_called_once_with("./mocked_path/test_folder")
        mocked_os_mkdir.assert_called_once_with("./mocked_path/test_folder")
        mocked_open.assert_called_once_with("./mocked_path/test_folder/__init__.py", "w")
        mocked_file.close.assert_called_once_with()


else:

    @mock.patch("__builtin__.open")
    @mock.patch("os.mkdir")
    @mock.patch("os.path.exists")
    def test_mkdir_with_os_access(mocked_os_path_exists, mocked_os_mkdir, mocked_open):
        """
        Unit: asserts that os mkdir is called when the folder does not exist.
        """
        cls_dict = {"folder": "test_folder", "path": "./mocked_path"}
        mocked_os_path_exists.return_value = False
        mocked_file = mock.Mock()
        mocked_open.return_value = mocked_file

        # method invocation
        pymkdir("./mocked_path/test_folder", cls_dict)

        # mock assertions
        mocked_os_path_exists.assert_called_once_with("./mocked_path/test_folder")
        mocked_os_mkdir.assert_called_once_with("./mocked_path/test_folder")
        mocked_open.assert_called_once_with("./mocked_path/test_folder/__init__.py", "w")
        mocked_file.close.assert_called_once_with()
