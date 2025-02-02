class Identify:
    def __init__(self, string=''):
        self.instring = ""
        self.command = ""
        self.words = []
        if string != '':
            self.instring = string
            self.words = string.split()
            self.command = self.words[0]
            
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
