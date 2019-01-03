"""
Module with unit tests for the python_mkdir function.
"""
import os
import sys

from pymkdir.main import python_mkdir

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
@mock.patch("os.path.exists")
@mock.patch("pymkdir.main.get_command_line_args")
def test_python_mkdir_with_os_access_no_path_exists(
    mocked_get_command_line_args, mocked_os_path_exists, mocked_pymkdir, mocked_os_access
):
    """
    Unit: asserts that pymkdir is called when os access is not restricted.
    """
    # mock responses
    cls_dict = {"folder": "test_folder", "path": "./mocked_path"}

    mocked_get_command_line_args.return_value = cls_dict
    mocked_os_access.return_value = True  # no OS restriction
    mocked_os_path_exists.return_value = False  #  path does NOT exist

    # method invocation
    python_mkdir()

    # mock invocation assertions
    mocked_os_access.assert_called_once_with("./mocked_path", os.W_OK)
    mocked_os_path_exists.assert_called_once_with("./mocked_path/test_folder")
    mocked_pymkdir.assert_called_once_with("./mocked_path/test_folder", cls_dict)
