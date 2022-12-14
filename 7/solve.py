from rich import print as rprint
import re

"""
cd means change directory.
    cd x moves in one level
    cd .. moves out one level
    cd / switches the current directory to the outermost directory, /.
ls means list.
    123 abc means that the current directory contains a file named abc with size 123.
    dir xyz means that the current directory contains a directory named xyz.

Given the commands and output in example.txt, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

"""


def is_command(input) -> bool:
    return input[0] == "$"


def is_cd(input) -> bool:
    return input[0:4] == "$ cd"


def is_dir(input) -> bool:
    return input[0:3] == "dir"


def dir_name(input) -> str:
    return input[4:]


def cd_target(input) -> str:
    return input[5:]


def is_ls(input) -> bool:
    return input[0:4] == "$ ls"


def is_file(input) -> bool:
    return re.match(r"^[0-9]+ ", input) is not None


def file_name(input) -> str:
    match = re.match(r"^[0-9]+ (.*?)$", input)
    return match[1]


def file_size(input) -> str:
    match = re.match(r"^([0-9]+) (.*?)$", input)
    return match[1]


class AocFile:
    pass


class AocDirectory:
    pass


class AocDirectory:
    def __init__(self, name: str):
        self._name = name
        self._directories = []
        self._files = []

    def add_file(self, fle: AocFile):
        self._files.append(fle)

    def add_dir(self, dr: AocDirectory):
        self._directories.append(dr)


class AocFile:
    def __init__(self, name: str, size: int, directory: AocDirectory):
        self._name = name
        self._size = size
        self._parent_directory = directory


directory_structure = {}


with open('example.txt') as f:
    content_lines = f.read().split("\n")

    indent = ""
    curdir = None
    dirname = None

    for line in content_lines:
        iscommand = is_command(line)
        iscd = is_cd(line)
        cdtarget = cd_target(line)

        isls = is_ls(line)
        isfile = is_file(line)

        isdir = is_dir(line)
        if isdir:
            dirname = dir_name(line)

        if iscommand:
            if iscd:
                if cdtarget != "..":
                    curdir = cdtarget
                    directory_structure[curdir] = AocDirectory(curdir)
            if isls:
                continue

        if isfile:
            fl = AocFile(
                file_name(line),
                file_size(line),
                directory_structure[curdir])

            directory_structure[curdir].add_file(fl)

        # if isfile:
        #     filename = file_name(line)
        #     filesize = file_size(line)
        #     print(f"{indent}- {filename} (file, size={filesize})")

        # if isdir:
        #     dirname = dir_name(line)
        #     object = AocDirectory(dirname)

        # print(f"{line} \t\t\t is_command: {iscommand} | is_cd: {iscd} | cd_target: {cdtarget}")

# rprint(directory_structure)

for d in directory_structure:
    rprint(d)
