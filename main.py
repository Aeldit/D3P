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
from os import mkdir
from os.path import exists

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


def main(versions):
    for version in versions:
        if not exists(version):
            mkdir(version)

        # TODO: Change the output file the the corresponding file in the output directory
        with open("%s/output.mcfunction" % version, "w") as wf:
            wf.write(parse_file_for_version(version))
    return None


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Missing version arguments")
        exit(1)

    main(args[1:])
