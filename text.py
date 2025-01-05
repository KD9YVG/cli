import os
import msvcrt  # For Windows-specific keyboard input handling

dir = input('File name/path: ')

class openFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'a+')
        self.file.seek(0)

try:
    file = openFile(dir) # Open the file in append mode
except FileExistsError:
    file = openFile(dir)  # Open the file in append mode
except PermissionError:
    print(f"Permission denied: Unable to create '{dir}'. Try relaunching the CLI as sudo.")
except Exception as e:
    print(f"An error occurred: {e}")

class textEdit:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'r+')
        self.text = self.file.readlines()
        self.cursor_x = 0
        self.cursor_y = len(self.text) - 1 if self.text else 0

    def save_file(self):
        with open(self.file_path, 'w') as file:
            file.writelines(self.text)

    def main(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            for i, line in enumerate(self.text):
                if i == self.cursor_y:
                    print(f"> {line}", end='')
                else:
                    print(f"  {line}", end='')
            print("\nPress 'Ctrl+Q' to quit, 'Ctrl+W' to move up, 'Ctrl+S' to move down.")
            print("Press 'Enter' to add a new line.")
            
            if os.name == 'nt':
                user_input = msvcrt.getch()
                if user_input == b'\x11':  # Ctrl+Q
                    break
                elif user_input == b'\x17':  # Ctrl+W
                    self.cursor_y = max(0, self.cursor_y - 1)
                elif user_input == b'\x13':  # Ctrl+S
                    self.cursor_y = min(len(self.text) - 1, self.cursor_y + 1)
                elif user_input == b'\r':  # Enter key
                    self.text.insert(self.cursor_y + 1, '\n')
                    self.cursor_y += 1
                else:
                    user_input = input("Enter text: ")
                    if self.cursor_y < len(self.text):
                        self.text[self.cursor_y] = user_input + '\n'
                    else:
                        self.text.append(user_input + '\n')
                    self.cursor_y = len(self.text) - 1
            else:
                user_input = input("Enter text: ")
                if user_input.lower() == 'q':
                    break
                elif user_input.lower() == 'w':
                    self.cursor_y = max(0, self.cursor_y - 1)
                elif user_input.lower() == 's':
                    self.cursor_y = min(len(self.text) - 1, self.cursor_y + 1)
                elif user_input == '':
                    self.text.insert(self.cursor_y + 1, '\n')
                    self.cursor_y += 1
                else:
                    if self.cursor_y < len(self.text):
                        self.text[self.cursor_y] = user_input + '\n'
                    else:
                        self.text.append(user_input + '\n')
                    self.cursor_y = len(self.text) - 1
            self.save_file()

try:
    textEdit(dir).main()
except KeyboardInterrupt:
    exit(0)