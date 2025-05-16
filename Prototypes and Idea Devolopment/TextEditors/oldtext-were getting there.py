"""
pyText 0.0.1 Alpha - A simple text editor.

Usage:
    python text.py <file_path>

If <file_path> is not provided, a default file (buffer.tmp) is used.
"""

import blessed
import sys

term = blessed.Terminal()

# Retrieve file path from command-line arguments, using "buffer.tmp" as default.
path = sys.argv[1] if len(sys.argv) > 1 else "buffer.tmp"


class Text:
    """
    Handles file operations and terminal display for the text editor.
    Loads file content if a valid file path is provided and renders a stylized header.
    """
    def __init__(self):
        self.text = ""
        if path != "buffer.tmp":
            self.read_file(path)
        else:
            # Create the buffer file if no valid file path is provided.
            with open('buffer.tmp', 'w+') as f:
                pass

        self.display_header()

    def read_file(self, file_path):
        """
        Read file content from the specified file.

        Parameters:
            file_path (str): The path to the file.
        """
        try:
            with open(file_path, 'r') as file:
                self.text = file.read()
        except Exception as e:
            print(term.clear)
            sys.exit(
                f"Error: NO EDIT PERMISSIONS IN FOLDER.\n"
                f"{term.blue}Use text -r <filename> to open a file in read mode. Exception: {e}"
            )

    def display_header(self):
        """
        Clears the terminal and displays a centered header with a decorative border.
        """
        print(term.clear)
        header = " pyText 0.0.1 Alpha "
        border = "=" * len(header)
        print(term.center(border))
        print(term.center(term.on_white(term.black(header))))
        print(term.center(border))
        print(term.move_down)

    def setModeWrite(self, mode):
        """
        Set the editor to write mode if permissions allow.

        Parameters:
            mode (str): A string indicating the desired write mode.

        This method currently only displays a message indicating the write mode.
        """
        print(term.move_down)
        print(term.center(f"Entering write mode: {mode}"))
        # ... implement the write mode logic here ...


def main():
    """
    Launch the pyText editor.
    """
    try:
        editor = Text()
        # Placeholder for additional functionality.
        print(term.center("Editor is now running..."))
        print(term.center("THIS IS TEMPORARY"))
    except KeyboardInterrupt:
        # Clean exit on keyboard interrupt.
        sys.exit(0)


if __name__ == '__main__':
    main()