#!/usr/bin/env python3
"""
Pycture main code
"""

from src.parse_argv import parse_argv


def pycture() -> None:
    """
    Main function
    """
    args = parse_argv()


if __name__ == "__main__":
    pycture()