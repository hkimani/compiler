from common.regex import Regex
from colorama import init, Fore, Back, Style

init()

regex = Regex()


class Scanner:
    def __init__(self):

        """ TOKENS are listed in order of priority """

        # Functions for token type identification
        self.tokens = {
            "FLOAT": self.token_float,
            "IDENTIFIER": self.token_id,
            "INTEGER": self.token_int,
            "OPERATOR": self.token_operator,
            "STRING": self.token_string,
            "EXPRESSION": self.token_exp,
        }

        # Buffer string of characters that will be used to check for token validity
        self.tmp_string = ""
        self.token_type = ""

        # Errors
        self.errors = []

        # Match token type
        self.matched_function = None
        self.matched_tokens = []

    def start(self, source):
        # Padding to allow detection of last character
        source += " "

        # Iterator
        i = 0

        # Get token types
        while i < len(source):
            self.tmp_string += source[i]

            valid_token = self.check_token()

            # Check the character that has made the token invalid
            if not valid_token:
                self.tmp_string = source[i]
                self.check_token()

            # Move one step
            i += 1

        # Clean up false positives and vice versa
        self.cleanup()

    def error_found(self):
        self.errors.append(
            f"Error: The string {self.tmp_string} doesn't match any token pattern"
        )

    def check_token(self):

        if self.matched_function != None:
            matched = self.matched_function()
            if not matched:
                # Everything except last character
                valid_token = self.tmp_string[:-1]

                self.matched_tokens.append(
                    {"type": self.token_type, "value": valid_token}
                )
                self.tmp_string = ""
                self.token_type = ""

                self.matched_function = None
                return False
            else:
                return True
        else:
            for key in self.tokens:
                match_function = self.tokens[key]
                if match_function():
                    self.matched_function = match_function
                    self.token_type = key
                    return True

            # If no matching token has been found
            if not self.matched_function:
                self.error_found()
                self.tmp_string = ""
                self.token_type = ""
                return False

    def token_keyword(self, string):
        matched = regex.check_K(string)
        return matched

    def token_float(self):
        return regex.check_F(self.tmp_string)

    def token_id(self):
        # First character of array
        head_char = self.tmp_string[0]

        if not regex.check_CL(head_char):
            return False
        elif regex.check_CLI(self.tmp_string):
            return True
        else:
            return False

    def token_int(self):
        return regex.check_I(self.tmp_string)

    def token_operator(self):
        return regex.check_Op(self.tmp_string)

    def token_string(self):
        return regex.check_ST(self.tmp_string)

    def token_exp(self):
        return regex.check_EXP(self.tmp_string)

    def results(self):
        print(
            f"\nScanner finished with {Fore.RED}{len(self.errors) - 1} errors{Style.RESET_ALL} and found {Fore.GREEN}{len(self.matched_tokens)} tokens.{Style.RESET_ALL} \n"
        )
        print("Errors: ")

        for idx, error in enumerate(self.errors):
            # The padding we added at the end of the source code is a false positive. Last entry is ignored
            if not error == self.errors[-1]:
                print(Fore.RED + error + Style.RESET_ALL)

        print("\nTokens: ")
        for token in self.matched_tokens:
            print(
                f"<type: {Fore.GREEN}{token['type']}{Style.RESET_ALL}, value: {Fore.CYAN}{token['value']}{Style.RESET_ALL} >"
            )

    def cleanup(self):

        for token in self.matched_tokens:
            # Extract keywords from identifiers
            if self.token_keyword(token["value"]):
                token["type"] = "KEYWORD"

            # Update buffer
            self.tmp_string = token["value"]

            # Convert false positive from FLOAT to INTEGER
            if self.token_int():
                token["type"] = "INTEGER"
