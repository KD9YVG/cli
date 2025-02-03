global run
run = False

class cmdIdentify:
    def __init__(self, string=''):
        self.instring = ""
        self.command = ""
        self.words = []
        if string != '':
            self.instring = string
            self.words = string.split()
            self.command = self.words[0]
            global run
            run = True
            
    def demo(self, instring):
        self.instring = instring
        self.words = instring.split()
        if self.words:
            self.command = self.words[0]

    def get_instring(self):
        return self.instring

    def get_words(self):
        return self.words

    def get_command(self):
        return self.command

class cmdhandle:
    def identify(self, instring):
        global run
        if run == True:
            command = cmdIdentify.get_command()
            with open('Files/commands.txt', 'r') as file:
                # read the file line by line
                for line_num, line in enumerate(file, 1):
                    # check if the command is in the file
                    if command in line:
                        print(f"Line {line_num}: {line}")
                        break
                else:
                    print('Command not found')

cmdIdentify(input())
cmdhandle().identify(input())