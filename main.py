# ANSI codes for colors
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

BRIGHT_BG_BLACK = "\033[100m"
BRIGHT_BG_RED = "\033[101m"
BRIGHT_BG_GREEN = "\033[102m"
BRIGHT_BG_YELLOW = "\033[103m"
BRIGHT_BG_BLUE = "\033[104m"
BRIGHT_BG_MAGENTA = "\033[105m"
BRIGHT_BG_CYAN = "\033[106m"
BRIGHT_BG_WHITE = "\033[107m"

class UserInput:
    def __init__(self):
        self.instring = input()
    
    def print_input(self):
        print(self.instring)

    def cmd(self):
        if self.instring == "exit":
            exit(0)
        elif self.instring.startswith('echo '):
            # Extract the part of the string after 'echo '
            message = self.instring[len('echo '):]
            print(message)
        elif self.instring == 'clear':
            print("\033[H\033[J")
        else:
            print(RED + self.instring + RESET + f', Command not found. For more information, type "{YELLOW}help{RESET}".')

while True:
    UserInput().cmd()