"""
Package code into a zip file

Public Functions:
    packaged_code: Yields bytes of packaged code
"""

from pathlib import Path
from typing import Generator
from zipfile import ZipFile, PyZipFile
from tempfile import TemporaryFile, TemporaryDirectory

_EXTENSIONS: set[str] = {".pyc"}
_EXCLUDED_FILES: set[str] = set()
_EXCLUDED_DIRS: set[str] = {"tests"}


def packaged_code(base_path: Path) -> bytes:
    """
    Package code into a zip file, and return the raw zip bytes

    Args:
        base_path (pathlib.Path): Base path of the project

    Returns:
        (bytes): Raw bytes of the packaged code
    """
    with TemporaryFile("w+b") as fp:
        if base_path.is_dir():
            with PyZipFile(fp, "w") as pzf:
                pzf.writepy(base_path / "__main__.py")  # type: ignore
                pzf.writepy(base_path / "utils")  # type: ignore
        elif base_path.is_file():
            with TemporaryDirectory() as new_path_str:
                new_path = Path(new_path_str)
                zipped = ZipFile(base_path)
                zipped.extractall(new_path)
                with PyZipFile(fp, "w") as pzf:
                    for script_path in _walk_path(new_path):
                        pzf.write(script_path, script_path.relative_to(new_path))
        else:
            raise OSError(f"{base_path} is not a directory or a file")
        fp.seek(0)
        return fp.read()


def _walk_path(dir_path: Path) -> Generator[Path, None, None]:
    """
    Walk through a directory and generate paths with a specific extension

    Args:
        dir_path (pathlib.Path): Directory path
    """
    for sub_path in dir_path.iterdir():
        if sub_path.is_dir():
            if sub_path.name in _EXCLUDED_DIRS:
                continue
            yield from _walk_path(sub_path)
        elif sub_path.is_file():
            if sub_path.suffix not in _EXTENSIONS:
                continue
            if sub_path.stem in _EXCLUDED_FILES:
                continue
            yield sub_path
