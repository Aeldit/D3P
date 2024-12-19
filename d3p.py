#!/bin/env python3
"""
:author: Aeldit <https://github.com/Aeldit>

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
from os import listdir, makedirs, mkdir
from os.path import dirname, exists, isdir, isfile
from shutil import rmtree

RANGES = {
    "1.13.x": ("1.13", "1.13.1", "1.13.2"),
    "1.14.x": ("1.14", "1.14.1", "1.14.2", "1.14.3", "1.14.4"),
    "1.15.x": ("1.15", "1.15.1", "1.15.2"),
    "1.16.x": ("1.16", "1.16.1", "1.16.2", "1.16.3", "1.16.4", "1.16.5"),
    "1.17.x": ("1.17", "1.17.1"),
    "1.18.x": ("1.18", "1.18.1", "1.18.2"),
    "1.19.x": ("1.19", "1.19.1", "1.19.2", "1.19.3", "1.19.4"),
    "1.20.x": (
        "1.20",
        "1.20.1",
        "1.20.2",
        "1.20.3",
        "1.20.4",
        "1.20.5",
        "1.20.6",
    ),
    "1.21.x": ("1.21", "1.21.1", "1.21.2", "1.21.3", "1.21.4"),
}
RANGES_KEYS = RANGES.keys()


def get_files_tree(datapack_path: str) -> dict[str, tuple]:
    """
    Stores all the files found in the sub-directories of the given path
    """
    # Puts each file as a full path, because otherwise the files aren't found
    paths_stack = [
        "%s/%s" % (datapack_path, file) for file in listdir(datapack_path)
    ]

    files = dict()

    while len(paths_stack) != 0:
        file = paths_stack.pop()

        if isdir(file):
            paths_stack.extend(["%s/%s" % (file, f) for f in listdir(file)])

        elif isfile(file):
            if file.endswith(".mcfunction"):
                with open(file, "r") as rf:
                    files[file] = tuple(rf.readlines())
            else:
                with open(file, "rb") as rf:
                    files[file] = tuple(rf.read())
    return files


def find_all_versions(files: dict[str, tuple]) -> set[str]:
    """
    Iterates through all files and sub-directories in the given datapack
    directory and stores which versions are used with the preprocessor

    :param datapack_path: The path to the datapack folder
    :returns: A set containing all the versions that were found
    """
    versions = set()
    for file, lines in files.items():
        if not exists(file) or not file.endswith(".mcfunction"):
            continue

        for version in tuple(
            line.split("=")[1].removesuffix("\n")
            for line in lines
            if type(line) is str
            and line.startswith("#ver=")
            and not len(line.split("=")[1].removesuffix("\n")) == 0
        ):
            if version not in versions:
                versions.add(version)
    return versions


def parse_file_for_version(
    version: str, lines: tuple[str], strip_comments: bool
) -> str:
    """
    Parses the given lines and creates from them a string that contains only
    the code concerning the given version

    :param version: The version to use for the current parsing
    :param lines: The lines of the file
    :param strip_comments: Whether to keep the comments or not
    :returns: The string parsed for the given version
    """
    parsed = []
    should_take_line = True

    for line in lines:
        if line.startswith("#ver="):
            ver = line.split("=")[1].removesuffix("\n")

            if ver != version:
                # Range in the form '1.20.x-1.21.x'
                if ver.count("-") == 1:
                    should_take_line = any(
                        version in RANGES[v]
                        for v in ver.split("-")
                        if v in RANGES_KEYS
                    )

                # Simple '1.XX.x' version
                elif ver.endswith(".x") and ver in RANGES_KEYS:
                    should_take_line = version in RANGES[ver]

                # Invalid preprocessor directive
                else:
                    should_take_line = False
            else:
                should_take_line = True
            continue

        elif line.startswith("#endver"):
            should_take_line = True
            continue

        if should_take_line and not (
            strip_comments and line.strip().startswith("#")
        ):
            parsed.append(line)

    return "".join(parsed)


def generate_pack_for_version(
    version: str, files: dict[str, tuple], pack_path: str, strip_comments: bool
) -> None:
    """
    Generates the same directory tree as the datapack, but with the version as
    root directory and by applying the preprocessing to the mcfunction files

    :param version: The version as a string
    :param files: A dict in the form directory:listdir(directory)
    :param strip_comments: Whether to keep the comments or not
    :param pack_path: The path to the root directory of the pack
    """
    if exists(version):
        rmtree(version)
    mkdir(version)

    for file, lines in files.items():
        if lines is None:
            continue

        new_file = file.replace(pack_path, version)
        makedirs(dirname(new_file), exist_ok=True)

        if all(type(line) is str for line in lines):
            with open(new_file, "w") as wf:
                wf.write(parse_file_for_version(version, lines, strip_comments))
        elif all(type(line) is int for line in lines):
            with open(new_file, "wb") as wf:
                wf.write(bytes(lines))
    return None


def main(datapack_path: str, strip_comments: bool) -> int:
    if not exists(datapack_path):
        print("The specified path does not exist ('%s')" % datapack_path)
        return 1

    files = get_files_tree(datapack_path)
    for version in find_all_versions(files):
        print(version)
        generate_pack_for_version(version, files, datapack_path, strip_comments)
    return 0


if __name__ == "__main__":
    usage = (
        "Usage:\n    ./d3p.py -d /path/to/datapack_folder [-OPTION]\n\nOptions:"
        "\n    -sc: Strip Comments\n        Remove comments from each "
        "mcfunction file"
    )

    args = sys.argv

    if "-d" not in args:
        print(usage)
        exit(1)

    d_idx = args.index("-d")
    if len(args) < d_idx + 1:
        print(usage)
        exit(1)

    exit(main(args[d_idx + 1], "-sc" in args))
