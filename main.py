## TODO ##
##########
# Add more commands
# Add text editor

from Files import colors as color
from Files import cmdhandle as cmdhdl

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
        elif self.instring == 'clear' or self.instring == 'cls':
            print("\033[H\033[J")
        elif self.instring == 'help':
            with open('Files/help.txt', 'r') as f:
                contents = f.read()
                # Split at the period to color first sentence
                first_sentence, rest = contents.split('.', 1)
                print(color.BG_RED + first_sentence + '.' + color.RESET + rest)
        elif self.instring.startswith('text'):
            print('Text editor')
        elif self.instring == 'cmdhandledemo':
            cmd = cmdhdl.Identify()
            cmd.demo(input('CMDHANDLE Demo: '))
            print(cmd.get_instring())
            print(cmd.get_words())
            print(cmd.get_command())
        else:
            print(color.RED + self.instring + color.RESET + f', Command not found. For more information, type "{color.YELLOW}help{color.RESET}".')

while True:
    try:
        print(f'{color.GREEN}OK {color.BLUE}$ {color.RESET}', end='')
        UserInput().cmd()
    except KeyboardInterrupt:
        print(color.RED + '\nExit' + color.RESET)
        exit(0)