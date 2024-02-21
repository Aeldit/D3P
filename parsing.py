IFDEF_LEN = 6
ELSEIFDEF_LEN = 10
ENDIF_LEN = 6


def parse_file(version: str):
    with open("test.mcfunction", "r") as rf:
        lines = rf.readlines()
    rf.close()

    parsed = []

    is_condition_met = True

    for line in lines:
        line_len = len(lines)
        if line[0] == "#":
            if line_len > IFDEF_LEN + 1 and line[1:IFDEF_LEN] == "ifdef":
                is_condition_met = line[IFDEF_LEN + 1:-1] == version

            elif line_len > ELSEIFDEF_LEN + 1 and line[1:ELSEIFDEF_LEN] == "elseifdef":
                is_condition_met = line[ELSEIFDEF_LEN + 1:-1] == version

            elif line_len > ENDIF_LEN + 1 and line[1:ENDIF_LEN] == "endif":
                is_condition_met = True

            elif is_condition_met is not False:
                parsed.append(line)

        elif is_condition_met is not False:
            parsed.append(line)

    return "".join(parsed)
