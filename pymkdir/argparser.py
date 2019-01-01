"""
Module which holds all the functions required to parse command line
arguments.
"""
import argparse
from typing import Dict, Optional


def get_command_line_args() -> Dict[str, Optional[str]]:
    """
    Command line arguments parser. Returns the command-line arguments
    that were input by the user.

    "-d/--directory": str to be used as an os path (optional);
    "-e/--empty": boolean whichi indicates no __init__.py creation (optional);

    Returns:
        dict: dictionary with command-line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--folder", required=True)
    parser.add_argument("-d", "--directory", default="./")
    parser.add_argument("-e", "--empty", default=None, nargs="?", const=True)

    args = vars(parser.parse_args())

    return args
