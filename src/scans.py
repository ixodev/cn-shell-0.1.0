# Written by Curtis Newton and Younès B.
# Read on a stream

import sys, datetime

for i in range(3, len(sys.argv)): print(f"{sys.argv[i]} ", end="")

print(f"[Written with CN-Shell on {datetime.datetime.now()}] ; " + input(": "), file=open(sys.argv[2], "a"))