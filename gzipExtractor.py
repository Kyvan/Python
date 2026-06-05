#!/home/ky/python_env/bin/python

import gzip
import os
import re
import shutil
from colorama import Fore, Back, Style
from pathlib import Path


_destination_folder = "/home/ky/testGround/"


def _gzip_content_finder(_exteracted_files):
    with Path(_exteracted_files).open() as _content:
        for _line in _content.readlines():
            _match = re.search("number0[0-5]", _line)
            if _match:
                print(f"{Style.BRIGHT}{Fore.CYAN}Line: {_match.group()}{Fore.RESET}")


def _gzip_extractor(_files):
    for _files in Path(_files).iterdir():
        if _files.is_file() and Path(_files).suffix == ".gz":
            _new_file = Path(_files).stem
            with gzip.open(_files, "rb") as f_in:
                with open(_new_file, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
            _gzip_content_finder(_new_file)
        else:
            print(f"{Style.BRIGHT}{Fore.RED}{Path(_files).name} is NOT valid{Fore.RESET}")
        

def _gzip_cleanup(_file_cleanup):
    for _file in Path(_file_cleanup).iterdir():
        if _file.is_file() and Path(_file).suffix == ".json":
            _file.unlink()


if Path(_destination_folder).is_dir():
    os.chdir(_destination_folder)
    _gzip_extractor(_destination_folder)
    _gzip_cleanup(_destination_folder)
