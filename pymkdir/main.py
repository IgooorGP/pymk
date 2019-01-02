"""
Main module.
"""
import os

from pymkdir.argparser import get_command_line_args
from pymkdir.mkdir import pymkdir


def python_mkdir():
    """
    Creates a folder with a __init__.py file in it at a file path
    determined by the user. Checks if the path exists, if there
    are writing permissions to it and if there's a folder there
    already.
    """
    command_line_args = get_command_line_args()

    folder_name = command_line_args.get("folder")
    file_path = os.path.join(command_line_args.get("path"))
    full_folder_path = os.path.join(file_path, folder_name)

    if os.access(os.path.dirname(full_folder_path), os.W_OK):

        if os.path.exists(full_folder_path):
            print(f"Ops! Looks like there's folder at {full_folder_path} already! Can't proceed.")

        else:
            pymkdir(full_folder_path, command_line_args)

    else:
        print(f"Sorry, no writing permission at the directory: {file_path}. Perhaps, use sudo?")


if __name__ == "__main__":
    python_mkdir()
