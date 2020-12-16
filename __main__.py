#!/usr/bin/env python3
"""
Pycture main code
"""

from utils.parse_argv import parse_argv
from utils.image_io import Image_IO


def pycture() -> None:
    """
    Main function
    """
    args = parse_argv()
    img_io = Image_IO(args.victim_path)
    original_data = img_io.read()


if __name__ == "__main__":
    pycture()