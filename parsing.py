def parse_file(version: str):
    with open("test.mcfunction", "r") as rf:
        lines = rf.readlines()
    rf.close()

    for line in lines:
        line_len = len(lines)
        if line[0] == "#":
            if line_len > 7 and line[1:6] == "ifdef":
                print(line)
            elif line_len > 12 and line[1:10] == "elseifdef":
                print(line)
            elif line_len > 7 and line[1:6] == "endif":
                print(line)
    return None
