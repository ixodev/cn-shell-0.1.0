# Written by Curtis Newton and Younès B.

import sys

NEW_DIR_PATH = ".." # Default value

try: NEW_DIR_PATH = sys.argv[1]
except Exception as err:
    print(f"An Exception occured. Reason: {err}")
    quit(0)

NEW_DIR_PATH = sys.argv[1]

