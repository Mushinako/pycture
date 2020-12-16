"""
Parsing command-line arguments for Pycture

Public Functions:
    parse_argv() -> _Args: Parsing arguments into Namespace object
"""

from __future__ import annotations
from argparse import ArgumentParser, Namespace, ArgumentTypeError
from pathlib import Path


def parse_argv() -> _Args:
    """
    Parse command-line arguments for Pycture

    Returns:
        (_Args): The Namespace object containing all the command-line arguments
    """
    parser = ArgumentParser(description="infect your image with my code!")
    parser.add_argument(
        "victim_path",
        type=_valid_path,
        help="path to the victim image file",
    )

    return parser.parse_args(namespace=_Args())


class _Args(Namespace):
    """
    Command-line arguments dataclass (not an actual dataclass)

    Class attributes:
        victim_path (pathlib.Path): A Path object pointing to the victim
    """

    victim_path: Path


def _valid_path(path_str: str) -> Path:
    """
    Check if a path is valid. If so, resolve and return it

    Args:
        path_str (str): A path string supposedly pointing to a file

    Returns:
        (pathlib.Path): Corresponding Path object with absolute path
    """
    path = Path(path_str)
    if not path.is_file():
        raise ArgumentTypeError(f"{path_str} is not a valid file")
    return path.resolve()
