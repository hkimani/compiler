from common.utilities import get_content, validate_arguments
from scanner.main import Scanner
import os
import sys

import re

# Exit if too many or too few arguments are given
exit() if validate_arguments(sys.argv) == False else None

# Convert relative path to absolute path.
path_to_source = os.path.abspath(sys.argv[1])

# Compressed source file
source = get_content(path_to_source)

# Start scanning
scanner = Scanner()
scanner.start(source)
scanner.results()
