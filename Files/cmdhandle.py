class identify:
    def __init__(self, string):
        self.string = string
        words = string.split()
        self.command = words[0]

class demo:
    def __init__(self):
        self.instring = input()
        print('\033[2J')
        print(self.instring)
        identify(self.instring)
        ## print(identify.words)
        print(identify.command)

demo()