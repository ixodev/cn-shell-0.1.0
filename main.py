# Written by Curtis Newton and Younès B.

try: import sys, os, platform, json, colorama, time, datetime
except ImportError as err: print(f"An ImportError occured. Reason: {err}", file=sys.stderr)

timestart = time.time()

# Constants
command: str

# Loading data from info.json
JSON_INFO_DATA = json.load(open("info.json"))

print(colorama.Fore.BLUE + f"CN-Shell {JSON_INFO_DATA['version']}, running on {platform.system()} {platform.version()}.")
print("CN-Shell, written by Curtis N. and Younès B.")
print(f"Execution on: {datetime.datetime.now()}")

while True:
    command = input(colorama.Fore.GREEN + f"CNShell-{JSON_INFO_DATA['version']} (stdin) -> ")
    cmd_without_args = command.split()

    # Built-in commands
    if command == "exit": break
    elif command == "cls": os.system("cls")
    elif command == "time": print(time.time())
    elif command == "des": print(JSON_INFO_DATA["description"])
    elif command == "authors": print(JSON_INFO_DATA["authors"])

    else:
        if cmd_without_args[0] + ".py" in os.listdir("src"): os.system(f"python src/{cmd_without_args[0]}.py {command}")
        else: print(colorama.Fore.RED + f"Error: unknown command: {command}.")

print(f"The execution lasted {time.time() - timestart} seconds. Bye!")
input()
quit(0)