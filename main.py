class UserInput:
    def __init__(self):
        self.instring = input()
    
    def print_input(self):
        print(self.instring)

for i in range(10):
    user_input = UserInput()
    user_input.print_input()