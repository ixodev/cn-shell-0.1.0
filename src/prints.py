# Written by Curtis Newton and Younès B.
# Write on stdout

import sys

for i in range(2, len(sys.argv)):
    if i != len(sys.argv) - 1: print(f"{sys.argv[i]} ", end="")
    else: print(f"{sys.argv[i]}")