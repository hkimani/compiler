"""
C = 'A..Z'
L = 'a..z'
CL = 'A..Z' | 'a..z'
CLI = 'A..Z' | 'a..z' | 0..9
W = 'White space'
S = 'Special characters'
I = 0 + (β)(∑)*
O = '0'
β = ' [1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9] '
E (∑) = ' [0 |1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9] '
F = 'I . I'
K = ' input + print + int + float + while + for + None + in + range '
Op = ' += |< | = | / | [ | ] |( | ) | , '
ST = 'I|W|S'
EXP = ' ; '

"""

import re


class Regex:
    def __init__(self):
        None

    # Check alphabet
    def check_CL(self, string):
        # Returns object if match is found
        return re.search("^[A-Za-z]*$", string)

    # Check alphanumerics
    def check_CLI(self, string):
        return re.search("^[a-zA-Z0-9_]+$", string)

    # Check keywords
    def check_K(self, string):
        keywords = [
            "input",
            "print",
            "len",
            "int",
            "float",
            "while",
            "for",
            "None",
            "in",
            "range",
        ]
        for keyword in keywords:
            if keyword == string:
                return True
        return False

    # Check 0
    def check_0(self, string):
        return re.search("^[0]+")

    # Check integers from 1 to 9
    def check_β(self, string):
        return re.search("^[1-9]+")

    # Check Integers from 1 to 9
    def check_E(self, string):
        return re.search("^[0-9]+")

    # Check integer
    def check_I(self, string):
        if re.search("^[0]{1}$", string) and (len(string) == 1):
            return True
        elif re.search("^[1-9][0-9]*$", string):
            return True
        else:
            return False

    # Check float
    def check_F(self, string):
        if self.check_I(string):
            return True
        elif self.check_I(string[:-1]) and string[-1] == ".":
            return True
        elif re.search("^[-+]?[0-9]*(\.[0-9]+)$", string):
            return True
        else:
            return False

    # Check operator
    def check_Op(self, string):
        check = re.search(
            "^(\+|\+=|\-=|\-|\*|\/|=|>|<|>=|<=|&|\||%|!|\^|\(|\)|\{|\})$", string
        )
        return check

    # Check string
    def check_ST(self, string):
        # Look for matching string with opening DOUBLE quotes and a body of characters
        if re.search('^"[^"]*$', string):
            return True

        # Look for matching string with full opening and closing DOUBLE quotes
        elif re.search('"[^"]*"$', string):
            return True

        # Look for matching string with opening SINGLE quotes and a body of characters
        elif re.search("^'[^']*$", string):
            return True

        # Look for matching string with full opening and closing SINGLE quotes
        elif re.search("^'[^']*'$", string):
            return True

        # Otherwise false
        else:
            return False

    # Check expression (Closing semi colon)
    def check_EXP(self, string):
        return re.search("^[;]$", string)
