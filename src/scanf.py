import sys

try: file = open(sys.argv[2], "r")
except Exception as err:
    print(f"An Exception occured. Reason: {err}")
    quit(0)

print(file.read())

file.close()