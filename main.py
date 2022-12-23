# Written by Curtis Newton and Younès B.

try: import sys, os, platform, json, colorama, time
except ImportError as err: print(f"An ImportError occured. Reason: {err}", file=sys.stderr)


# Constants
command: str

if len(sys.argv) <= 1: DEFAULT_DIR = f"C:/Users/{os.getlogin()}"
else: DEFAULT_DIR = sys.argv[1] # Make available for command arguments

DIR = DEFAULT_DIR

# Loading data from info.json
file = open("info.json")
JSON_INFO_DATA = json.load(file)
file.close()


print(colorama.Fore.BLUE + f"CN-Shell {JSON_INFO_DATA['version']}, running on {platform.system()} {platform.version()}.")
print(colorama.Fore.BLUE + "CN-Shell, written by Curtis N. and Younès B.")

while True:
    command = input(colorama.Fore.GREEN + f"{DIR} (stdin) -> ")
    cmd_without_args = command.split()

    # Built-in commands
    if command == "exit": quit(0)
    elif command == "cls": os.system("cls")
    elif command == "time": print(time.time())

    else:
        try: os.system(f"python src/{cmd_without_args[0]}.py {command}")
        except: print(colorama.Fore.RED + f"Error: unknown command: {command}")
