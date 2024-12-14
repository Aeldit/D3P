#!/bin/env python3
"""
D3P (DataPack PreProcessor)

The goal of this project is to add a syntax for preprocessed 'if's to the mcfunction language
Exemple :

#ver=1.20.4
code
#ver=1.19.3
other code
#endver
"""

import sys
from os import listdir
from os.path import exists, isdir, isfile

RANGES = {
    "1.19.x": ("1.19", "1.19.1", "1.19.2", "1.19.3", "1.19.4"),
    "1.20.x": ("1.20", "1.20.1", "1.20.2", "1.20.3", "1.20.4", "1.20.5", "1.20.6"),
    "1.21.x": ("1.21", "1.21.1", "1.21.2", "1.21.3", "1.21.4"),
}


def parse_file_for_version(version: str):
    with open("test.mcfunction", "r") as rf:
        lines = rf.readlines()

    parsed = []
    should_take_line = True

    for line in lines:
        if line.startswith("#ver="):
            ver = line.split("=")[1].removesuffix("\n")
            if version.endswith(".x"):
                should_take_line = ver == version or ver in RANGES[version]
            else:
                should_take_line = ver == version
            continue

        elif line.startswith("#endver"):
            should_take_line = True
            continue

        if should_take_line:
            parsed.append(line)

    return "".join(parsed)


def find_all_versions(datapack_path: str) -> set[str]:
    """
    Iterates through all files in the given datapack directory and stores
    which versions are used with the preprocessor

    :param datapack_path: The path to the datapack folder
    """
    versions = set()
    # Puts each file as a full path, because otherwise the files aren't found
    paths_stack = ["%s/%s" % (datapack_path, file) for file in listdir(datapack_path)]

    while len(paths_stack) != 0:
        file = paths_stack.pop()

        # If the file is a dir, we add all of its files with their full path
        if isdir(file):
            paths_stack.extend(["%s/%s" % (file, f) for f in listdir(file)])

        elif isfile(file) and file.endswith(".mcfunction"):
            with open(file, "r") as rf:
                lines = rf.readlines()

            for version in tuple(
                line.split("=")[1].strip()
                for line in lines
                if line.startswith("#ver=") and not len(line.split("=")[1].strip()) == 0
            ):
                if version not in versions:
                    versions.add(version)
    return versions


def main(datapack_path: str) -> int:
    if not exists(datapack_path):
        print("The specified path does not exist ('%s')" % datapack_path)
        return 1

    print(find_all_versions(datapack_path))
    return 0


if __name__ == "__main__":
    args = sys.argv

    if "-d" not in args:
        print("Datapack argument not specified (-d path/to/datapack)")
        exit(1)

    d_idx = args.index("-d")
    if len(args) < d_idx + 1:
        print("Datapack argument not specified (-d path/to/datapack)")
        exit(1)

    main(args[d_idx + 1])
