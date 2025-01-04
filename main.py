## TODO ##
##########
# Add more commands
# Move colors to another file
# Add a help command
# Update README.md

import colors as color

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
            print(color.RED + self.instring + color.RESET + f', Command not found. For more information, type "{color.YELLOW}help{color.RESET}".')

while True:
    UserInput().cmd()