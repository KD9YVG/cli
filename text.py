import blessed

term = blessed.Terminal()

class Text:
    def __init__(self):
<<<<<<< HEAD
        print(term.enter_fullscreen())
        print(term.clear)
        print(term.on_white(term.black('pyText 0.0.1 Alpha').center(term.width).ljust(term.width)))
        print(term.move_down)
        print(term.move_xy(0, term.height - 1) + term.on_white(term.black('Ctrl+X - Close    Ctrl+S - Save').ljust(term.width)))
        print(term.move_xy(0, 0))  # Position cursor right below the header

        # Create a dictionary to store the lines with the line number as the key.
        self.data = {}
        print("Enter text (press Enter on an empty line to finish):")
        line_num = 0
        while True:
            line = input()
            if line == "":
                break
            self.data[line_num] = line
            line_num += 1

        print("\nData entered:")
        for num, line in self.data.items():
            print(f"{num}: {line}")

Text()
print(term.exit_fullscreen())
=======
        print(term.center(term.on_white(term.black('pyText 0.0.1 Alpha'))))
        print(term.move_down)

Text()
>>>>>>> parent of 03cc37b (text.py now takes up full screen)
