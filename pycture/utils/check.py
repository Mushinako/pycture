"""
Do some checking before proceeding

Public Functions:
    check: One-stop checking solution
"""

from .footer import MAX_SIZE, UNIQ


def checks(img_bytes: bytes) -> bool:
    """
    Check if a image file can be infected

    Current checks include:
     - Image is not infected already
     - Image is within size limit

    Args:
        img_bytes (bytes): Raw image bytes

    Returns:
        (bool): Whether a file passes all checks
    """
    return _not_infected(img_bytes) and _within_size(img_bytes)


def _not_infected(img_bytes: bytes) -> bool:
    """
    Check if a file is not already infected
    """
    return img_bytes[-len(UNIQ) :] != UNIQ


def _within_size(img_bytes: bytes) -> bool:
    """
    Check if a file is within size limit (Currently 2 ** (256 * 8) bytes)
    """
    return len(img_bytes) <= MAX_SIZE
