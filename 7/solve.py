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


directory_structure = {
    '/': {
        'type': 'directory',
        'files': [],
        'directories': []
    },
}


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


with open('example.txt') as f:
    content_lines = f.read().split("\n")

    indent = ""

    for line in content_lines:
        iscommand = is_command(line)
        iscd = is_cd(line)
        cdtarget = cd_target(line)
        # dirname = dir_name(line)
        # isls = is_ls(line)
        isfile = is_file(line)
        isdir = is_dir(line)

        if iscommand and iscd:
            if cdtarget == "..":
                indent = indent[0:-2]
            else:
                print(f"{indent}- {cdtarget} (dir)")
                indent = indent + "  "

        if isfile:
            filename = file_name(line)
            filesize = file_size(line)
            print(f"{indent}- {filename} (file, size={filesize})")

        # print(f"{line} \t\t\t is_command: {iscommand} | is_cd: {iscd} | cd_target: {cdtarget}")

