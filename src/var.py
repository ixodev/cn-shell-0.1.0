# Written by Curtis Newton and Younès B.
import sys, os

try: os.system(f"set {sys.argv[1]} = {sys.argv[2]}")
except OSError as err: print(f"An OSError occured. Reason: {err}", file=sys.stderr)