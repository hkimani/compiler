from common.regex import Regex

regex = Regex()


class Scanner:
    def __init__(self):

        # TODO: ORDER TOKENS IN TERMS OF PRIORITY
        # todo: Reserved word has higher priority than identifier

        # Functions for token type identification
        self.tokens = {
            "TOKEN_ID": self.token_id,
            "TOKEN_EQUALS": self.token_equals,
            "TOKEN_LPAREN": self.token_lparen,
        }

        # Buffer string of characters that will be used to check for token validity
        self.tmp_string = ""

        # Errors
        self.errors = []

        # Match token type
        self.matched_function = None

        self.matched_tokens = []

    def start(self, source):
        i = 0

        while i < len(source):
            self.tmp_string += source[i]

            valid_token = self.check_token()

            # If the previously matched token is not valid
            if not valid_token and self.matched_function:
                # Move window back. Just after last valid token
                i -= 1
            else:
                # Advance
                i += 1

    def error_found(self):
        self.errors.append(
            f"Error: The string {self.tmp_string} doesn't match any token pattern"
        )

    def check_token(self):

        if self.matched_function != None:
            valid = self.matched_function()
            if not valid:
                # Everything except last character
                valid_token = self.tmp_string[:-1]
                # TODO: add details about identifier
                self.matched_tokens.append(valid_token)
                self.tmp_string = ""
                self.matched_function = None
                return False
            else:
                return True
        else:
            for match in self.tokens.values():
                if match():
                    self.matched_function = match
                    return True

            # If no matching token has been found
            if not self.matched_function:
                self.error_found()
                self.tmp_string = ""
                return False

        # Add error to errors list
        # self.errors.append(
        #     f"Error: The string {self.tmp_string} doesn't match any tokens"
        # )

        # # Reset buffer
        # self.tmp_string = ""

    def token_id(self):
        # First character of array
        head_char = self.tmp_string[0]

        if not regex.check_CL(head_char):
            return False
        elif regex.check_CLI(self.tmp_string):
            return True
        else:
            return False

    def token_equals(self):
        return False

    def token_lparen(self):
        return False

    def results(self):
        print(
            f"\nScanner finished with {len(self.errors)} errors and found {len(self.matched_tokens)} tokens.\n"
        )
        print("Errors: ")
        for error in self.errors:
            print(error)
        print("\nTokens: ")
        for token in self.matched_tokens:
            print(token)
