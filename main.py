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
    print("'%s'" % version)

    for line in lines:
        if line.startswith("#ver="):
            ver = line.split("=")[1].removesuffix("\n")
            if version.endswith(".x"):
                print(RANGES[version], "'%s'" % ver)
                should_take_line = ver == version or ver in RANGES[version]
                print(should_take_line)
            else:
                should_take_line = ver == version
            continue

        elif line.startswith("#endver"):
            should_take_line = True

        if should_take_line:
            parsed.append(line)

    return "".join(parsed)


def main():
    # TODO: Create a dir for each version
    for version in ("1.19.4", "1.20.x"):
        # TODO: Change the output file the the corresponding file in the output directory
        with open("output.mcfunction", "w") as wf:
            wf.write(parse_file_for_version(version))
    return None


if __name__ == "__main__":
    main()
