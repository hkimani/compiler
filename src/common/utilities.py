# Remove white spaces, trailing white spaces and newline breaks
def trim(line):
    return line.strip().replace(" ", "")


def get_content(path_to_file):
    file = open(path_to_file, "r")

    # array of all the lines in the source file
    lines = [trim(line) for line in file.readlines()]

    # a single unified string that has the source code
    source = "".join(lines)

    return source


def validate_arguments(arguments):
    if len(arguments) < 2:
        print("Error: Too few arguments given ...")
        return False
    elif len(arguments) > 2:
        print("Error: Too many arguments given ...")
        return False
    else:
        return True
