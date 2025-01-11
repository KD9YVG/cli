import os
import shutil

class OpenFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'a+')
        self.file.seek(0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

class TextEdit:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r+') as file:
            self.text = file.readlines()
        self.cursor_x = 0
        self.cursor_y = len(self.text) - 1 if self.text else 0
        self.current_line = ""

    def save_file(self):
        with open(self.file_path, 'w') as file:
            file.writelines(self.text)
        print("File saved successfully.")

    def main(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            columns, rows = shutil.get_terminal_size()
            header = f"Editing: {self.file_path} - Press 'Ctrl+Q' to quit"
            footer = "Press 'Ctrl+W' to move up, 'Ctrl+S' to move down, 'Enter' to add a new line, 'Ctrl+Q' to quit."

            print(f"\033[7m{header.center(columns)}\033[0m")  # Highlighted header
            for i, line in enumerate(self.text):
                if i == self.cursor_y:
                    print(f"> {line.rstrip()}{self.current_line}", end='')
                else:
                    print(f"  {line.rstrip()}", end='')

            # Fill the remaining lines with empty lines
            for _ in range(rows - len(self.text) - 4):
                print()

            print(f"\033[7m{footer.center(columns)}\033[0m")  # Highlighted footer

            user_input = input("Enter command (or text): ")
            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 'w':
                self.cursor_y = max(0, self.cursor_y - 1)
                self.current_line = ""
            elif user_input.lower() == 's':
                self.cursor_y = min(len(self.text) - 1, self.cursor_y + 1)
                self.current_line = ""
            elif user_input == '':
                if self.current_line:
                    if self.cursor_y < len(self.text):
                        self.text[self.cursor_y] = self.text[self.cursor_y].rstrip() + self.current_line + '\n'
                    else:
                        self.text.append(self.current_line + '\n')
                self.text.insert(self.cursor_y + 1, '\n')
                self.cursor_y += 1
                self.current_line = ""
            else:
                self.current_line += user_input
            self.save_file()

def main():
    dir = input('File name/path: ')
    try:
        with OpenFile(dir) as file:
            pass  # Open the file in append mode
    except PermissionError:
        print(f"Permission denied: Unable to create '{dir}'. Try relaunching the CLI as sudo.")
    except FileNotFoundError:
        print(f"File not found: '{dir}'. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        try:
            TextEdit(dir).main()
        except KeyboardInterrupt:
            print("\nExiting text editor.")
            exit(0)

if __name__ == "__main__":
    main()