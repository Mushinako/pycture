"""
Image file IO

Public Class:
    Image_IO(pathlib.Path): Class to handle image IO
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
        read ()      -> bytes: Read image raw bytes
        write(bytes) -> None : Write image raw bytes
    """

    def __init__(self, path: Path) -> None:
        self.path = path

    def read(self) -> bytes:
        """
        Read image raw bytes

        Returns:
            (bytes): Raw image bytes
        """
        with self.path.open("rb") as fp:
            return fp.read()

    def write(self, data: bytes) -> None:
        """
        Write image raw bytes

        Args:
            data (bytes): Modded image bytes
        """
        with self.path.open("wb") as fp:
            fp.write(data)
