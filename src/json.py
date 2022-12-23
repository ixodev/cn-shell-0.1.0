# Written by Curtis Newton and Younès B.
# Read & write JSON

import sys, json

try: file = open(sys.argv[2])
except Exception as err:
    print(f"An Exception occured. Reason: {err}")
    quit(0)

data = json.load(file)
file.close()

for attr in data: print(attr)

