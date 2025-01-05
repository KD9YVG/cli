import os

dir = input('File name/path: ')

class openFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'w')

try:
    file = openFile(dir, w+)
except FileExistsError:
    file = openFile(dir, r+)
except PermissionError:
    print(f"Permission denied: Unable to create '{dir}'. Try relaunching the CLI as sudo.")
except Exception as e:
    print(f"An error occurred: {e}")