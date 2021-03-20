import re

keywords = [
    "input",
    "print",
    "int",
    "float",
    "while",
    "for",
    "None",
    "in",
    "range",
]
# for keyword in keywords:
#     print(keyword.startswith("in"))

# for k in keywords:
#     print(k)


def check_I(string):
    if re.search("^[0]{1}$", string) and (len(string) == 1):
        return True
    elif re.search("^[1-9][0-9]*$", string):
        return True
    else:
        return False


v = re.search("^[0]{1}$", "0")
l = v and 1
# print(v and (len("0") > 2))
# print(check_I("2"))

print(re.search("^[;]$", ";"))
