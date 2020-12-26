"""
Footer of the infected file, stores some metadata
"""

from __future__ import annotations

import math


# Unique identifier
UNIQ = rb"HeyMushi" * 8
# Number of bytes to store original picture size
_SIZE_LENGTH_LENGTH = 1
# Max original picture size length
_MAX_SIZE_LENGTH = 1 << (_SIZE_LENGTH_LENGTH * 8)
# Max original picture size
MAX_SIZE = 1 << (_MAX_SIZE_LENGTH * 8)
# Big-endian for better reading during debug
_BYTE_ORDER = "big"


def create_footer(img_bytes: bytes) -> _Footer:
    """
    Create footer from uninfected image bytes

    Args:
        img_bytes (bytes): Uninfected image bytes

    Returns:
        (_Footer): Footer data
    """
    return _Footer.create(img_bytes)


def read_footer(img_bytes: bytes) -> _Footer:
    """
    Read footer from infected image bytes

    Args:
        img_bytes (bytes): Infected image bytes

    Returns:
        (_Footer): Footer data
    """
    return _Footer.read(img_bytes)


class _Footer:
    """
    Object containing footer data

    Public Readonly Properties:
        size   (int)  : Original image file size
        bytes_ (bytes): Footer bytes

    Class Methods:
        create: Create a footer from uninfected image bytes
        read  : Read a footer from infected image bytes
    """

    def __init__(self, size: int) -> None:
        if size > MAX_SIZE:
            raise ValueError(f"Size too big: {size}")
        self._size = size
        self._bytes = self._to_bytes()

    @property
    def size(self) -> int:
        return self._size

    @property
    def bytes_(self) -> bytes:
        return self._bytes

    def _to_bytes(self) -> bytes:
        """
        Convert footer info to bytes representation
        """
        num_bytes = math.ceil(math.log(self._size, 1 << 8))
        return (
            self._size.to_bytes(num_bytes, _BYTE_ORDER)
            + num_bytes.to_bytes(_SIZE_LENGTH_LENGTH, _BYTE_ORDER)
            + _SIZE_LENGTH_LENGTH.to_bytes(1, _BYTE_ORDER)
            + UNIQ
        )

    @classmethod
    def create(cls, img_bytes: bytes) -> _Footer:
        """
        Create a footer from uninfected image bytes
        """
        size = len(img_bytes)
        return cls(size)

    @classmethod
    def read(cls, img_bytes: bytes) -> _Footer:
        """
        Read a footer from infected image bytes
        """
        trimmed_bytes = img_bytes[: -len(UNIQ)]
        size_length_length = trimmed_bytes[-1]
        trimmed_bytes = trimmed_bytes[:-1]
        size_length = int.from_bytes(trimmed_bytes[-size_length_length:], _BYTE_ORDER)
        trimmed_bytes = trimmed_bytes[:-size_length_length]
        size = int.from_bytes(trimmed_bytes[-size_length:], _BYTE_ORDER)
        return cls(size)
