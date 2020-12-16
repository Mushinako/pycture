"""
Package code into a zip file
"""

from pathlib import Path
from zipfile import PyZipFile
from tempfile import TemporaryFile


def packaged_code(base_path: Path) -> bytes:
    """
    Package code into a zip file, and return the raw zip bytes

    Args:
        base_path (pathlib.Path): Base path of the project

    Returns:
        (bytes): Raw bytes of the packaged code
    """
    tempfile = TemporaryFile("w+b")

    with PyZipFile(tempfile, "w") as pzf:
        pzf.writepy(base_path)  # type: ignore

    return tempfile.read()
