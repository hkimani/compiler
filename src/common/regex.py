"""
C = 'A..Z'
L = 'a..z'
CL = 'A..Z' | 'a..z'
CLI = 'A..Z' | 'a..z' | 0..9
W = 'White space'
S = 'Special characters'
I = 'Integers'
F = 'Float'
"""

import re


class Regex:
    def __init__(self):
        None

    def check_CL(self, string):
        # Returns object if match is found
        return re.search("^[A-Za-z]*$", string)

    def check_CLI(self, string):
        return re.search("^[a-zA-Z0-9]+$", string)
