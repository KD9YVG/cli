## TODO ##
##########
# Add more commands
# Add text editor

from Files.Libs import colors as color
from Files.Libs import cmdhandle as cmdhdl
import blessed

term = blessed.Terminal()

class Main:
    def __init__(self):
        self.instring = input()
    
    def print_input(self):
        print(self.instring)

    def cmd(self):
        if self.instring == "exit":
            print(term.exit_fullscreen())
            exit(0)
        elif self.instring.startswith('echo '):
            # Extract the part of the string after 'echo '
            message = self.instring[len('echo '):]
            print(message) 
        elif self.instring == 'clear' or self.instring == 'cls':
            print(term.clear)
        elif self.instring == 'help':
            with open('Files/help.txt', 'r') as f:
                contents = f.read()
                # Split at the period to color first sentence
                first_sentence, rest = contents.split('.', 1)
                print(color.BG_RED + first_sentence + '.' + color.RESET + rest)
        elif self.instring.startswith('text'):
            print('HaHa')
            exec(open("text.py").read())
            open("text.py").close()
        elif self.instring == 'cmdhandledemo':
            cmd = cmdhdl.Identify()
            cmd.demo(input('CMDHANDLE Demo: '))
            print(cmd.get_instring())
            print(cmd.get_words())
            print(cmd.get_command())
        else:
            print(color.RED + self.instring + color.RESET + f', Command not found. For more information, type "{color.YELLOW}help{color.RESET}".')

with term.fullscreen():
    while True:
        try:
            print(f'{color.GREEN}OK {color.BLUE}$ {color.RESET}', end='', flush=True)
            Main().cmd()
        except KeyboardInterrupt:
            print(term.exit_fullscreen())
            print(color.RED + '\nExit' + color.RESET)
            exit(0)