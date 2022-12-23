import sys

try: file = open(sys.argv[2], sys.argv[3])
except Exception as err:
    print(f"An Exception occured. Reason: {err}")
    quit(0)

for i in range(4, len(sys.argv)):
    if i != len(sys.argv) - 1: print(f"{sys.argv[i]} ", end="", file=file)
    else: print(f"{sys.argv[i]}", file=file)

file.close()