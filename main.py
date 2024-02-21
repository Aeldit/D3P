"""
D3P (DataPack PreProcessor)

The goal of this project is to add a syntax for preprocessed 'if's to the mcfunction language
Exemple :

#ifdef 1.20.4
code
#elseifdef
other code
#endif
"""

import parsing

VERSIONS = ["1.19.4", "1.20.x"]


def main():
    # Changes the versions strings to the correct syntax (ex: 1.20.x -> MC_1_20_x)
    for i in range(len(VERSIONS)):
        VERSIONS[i] = "MC_%s" % (VERSIONS[i].replace(".", "_"))

    for ver in VERSIONS:
        with open("output.mcfunction", "w") as wf:
            wf.write(parsing.parse_file(ver))
    return None


if __name__ == "__main__":
    main()
