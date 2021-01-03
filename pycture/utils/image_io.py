"""
Image file IO

Public Class:
    Image_IO: Class to handle image IO (which is just reading/writing raw bytes)
"""

from pathlib import Path


class Image_IO:
    """
    Read/write image file

    Args:
        path (pathlib.Path): Path of the image file

    Public Attributes:
        path (pathlib.Path): Path of the image file

    Public Instance Methods:
        read : Read image raw bytes
        write: Write image raw bytes
    """

    def __init__(self, path: Path) -> None:
        self.path = path

    def read(self) -> bytes:
        """
        Read image raw bytes
        """
        with self.path.open("rb") as fp:
            return fp.read()

    def write(self, data: bytes) -> None:
        """
        Write image raw bytes
        """
        with self.path.open("wb") as fp:
            fp.write(data)
