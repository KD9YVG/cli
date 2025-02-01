import curses
import os

def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()
    return [""]

def save_file(file_path, text):
    with open(file_path, 'w') as file:
        file.writelines(text)

def main(stdscr, file_path):
    # Initialize the screen
    curses.curs_set(1)  # Make the cursor visible
    stdscr.keypad(True)  # Enable special keys
    stdscr.timeout(100)  # Refresh every 100ms

    # Load the file content
    text = load_file(file_path)
    cursor_x = 0
    cursor_y = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Display the text
        for i, line in enumerate(text):
            stdscr.addstr(i, 0, line)

        # Move the cursor
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        if key == 259 and cursor_y > 0:  # Up arrow
            cursor_y -= 1
            cursor_x = min(cursor_x, len(text[cursor_y]))
        elif key == 258 and cursor_y < len(text) - 1:  # Down arrow
            cursor_y += 1
            cursor_x = min(cursor_x, len(text[cursor_y]))
        elif key == 260 and cursor_x > 0:  # Left arrow
            cursor_x -= 1
        elif key == 261 and cursor_x < len(text[cursor_y]):  # Right arrow
            cursor_x += 1
        elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:  # Backspace key
            if cursor_x > 0:
                text[cursor_y] = text[cursor_y][:cursor_x-1] + text[cursor_y][cursor_x:]
                cursor_x -= 1
            elif cursor_y > 0:
                cursor_y -= 1
                cursor_x = len(text[cursor_y])
                text[cursor_y] += text.pop(cursor_y + 1)
        elif key == curses.KEY_ENTER or key == 10:  # Enter key
            text.insert(cursor_y + 1, text[cursor_y][cursor_x:])
            text[cursor_y] = text[cursor_y][:cursor_x]
            cursor_y += 1
            cursor_x = 0
        elif key >= 32 and key <= 126:  # Printable characters
            if cursor_y < len(text):
                text[cursor_y] = text[cursor_y][:cursor_x] + chr(key) + text[cursor_y][cursor_x:]
                cursor_x += 1
            else:
                text.append(chr(key))
                cursor_y += 1
                cursor_x = 1
        elif key == 27:  # ESC key to exit
            break

    # Save the file content before exiting
    save_file(file_path, text)

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    curses.wrapper(main, file_path)
