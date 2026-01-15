#!/usr/bin/env python3
"""
A simple, efficient terminal-based text editor using curses.

Usage:
    python3 editor.py [filename]

Controls:
    Arrow Keys: Navigation
    Ctrl+S:     Save File
    Ctrl+Q:     Quit
    Esc:        Cancel input prompts
"""

import curses
import sys
import os
import re
from typing import List, Optional, Tuple


class TextEditor:
    """
    Main editor class managing the state, rendering, and input handling.
    """

    def __init__(self,
                 stdscr: 'curses.window',
                 filename: str = "untitled.txt"):
        self.stdscr = stdscr
        self.filename = filename

        # Editor State
        self.lines: List[str] = [""]
        self.cx: int = 0  # Cursor X (Column)
        self.cy: int = 0  # Cursor Y (Row)
        self.scroll_y: int = 0  # Vertical Scroll Offset
        self.is_modified: bool = False
        self.running: bool = True

        # Configuration
        self.height: int = 0
        self.width: int = 0
        self.line_num_width: int = 0

        # Colors
        self._setup_colors()

        # Syntax Highlighting Patterns
        # Detects comments, strings (including triple-quoted), keywords, and numbers
        self.syntax_regex = re.compile(
            r'(?P<COMMENT>#[^\n]*)'
            r'|(?P<STRING>(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\'|\"[^\"]*\"|\'[^\']*\'))'
            r'|(?P<KEYWORD>\b(def|class|import|return|if|else|elif|try|except|for|while|in|is|not|and|or|from|as|with|pass|break|continue|print|True|False|None)\b)'
            r'|(?P<NUMBER>\b\d+\b)')

        # Load initial file
        self.load_file(filename)

    def _setup_colors(self):
        """Initialize color pairs."""
        curses.start_color()
        curses.use_default_colors()
        # Pair 1: Status Bar (White text on Blue background)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        # Pair 2: Line Numbers (Yellow text)
        curses.init_pair(2, curses.COLOR_YELLOW, -1)
        # Syntax Highlighting Colors
        curses.init_pair(3, curses.COLOR_CYAN, -1)  # Keywords
        curses.init_pair(4, curses.COLOR_GREEN, -1)  # Strings
        curses.init_pair(5, curses.COLOR_RED, -1)  # Comments
        curses.init_pair(6, curses.COLOR_MAGENTA, -1)  # Numbers

    def load_file(self, filename: str):
        """Reads the file into the line buffer."""
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.lines = f.read().splitlines()
                if not self.lines:
                    self.lines = [""]
            except IOError:
                self.lines = ["Error loading file."]
        else:
            self.lines = [""]

    def save_file(self):
        """Saves the current buffer to disk."""
        try:
            with open(self.filename, 'w') as f:
                f.write("\n".join(self.lines))
            self.is_modified = False
            self.show_flash_message(f"Saved to {self.filename}")
        except IOError as e:
            self.show_flash_message(f"Error saving: {e}")

    def get_input(self, prompt: str, default: str = "") -> Optional[str]:
        """
        Renders a prompt in the status bar and waits for string input.
        Returns the string or None if cancelled (Esc).
        """
        curses.curs_set(1)
        input_str = default

        while True:
            # Render prompt
            self.stdscr.attron(curses.color_pair(1))
            text = (prompt + input_str).ljust(self.width)[:self.width]
            try:
                self.stdscr.addstr(self.height - 1, 0, text)
            except curses.error:
                pass  # Ignore error writing to bottom-right corner
            self.stdscr.attroff(curses.color_pair(1))

            self.stdscr.move(self.height - 1,
                             min(len(prompt) + len(input_str), self.width - 1))
            self.stdscr.refresh()

            key = self.stdscr.getch()

            if key in (10, 13):  # Enter
                return input_str
            elif key == 27:  # Esc
                return None
            elif key in (curses.KEY_BACKSPACE, 127, 8):
                if len(input_str) > 0:
                    input_str = input_str[:-1]
            elif 32 <= key <= 126:
                if len(prompt) + len(input_str) < self.width - 1:
                    input_str += chr(key)

    def show_flash_message(self, message: str):
        """Displays a temporary message in the status bar."""
        self.stdscr.attron(curses.color_pair(1))
        try:
            self.stdscr.addstr(self.height - 1, 0, message.ljust(self.width))
        except curses.error:
            pass
        self.stdscr.attroff(curses.color_pair(1))
        self.stdscr.refresh()
        curses.napms(800)  # Pause for 800ms

    def handle_navigation(self, key: int):
        """Handles cursor movement logic."""
        row_len = len(self.lines[self.cy])

        if key == curses.KEY_UP:
            if self.cy > 0:
                self.cy -= 1
        elif key == curses.KEY_DOWN:
            if self.cy < len(self.lines) - 1:
                self.cy += 1
        elif key == curses.KEY_LEFT:
            if self.cx > 0:
                self.cx -= 1
            elif self.cy > 0:
                self.cy -= 1
                self.cx = len(self.lines[self.cy])
        elif key == curses.KEY_RIGHT:
            if self.cx < row_len:
                self.cx += 1
            elif self.cy < len(self.lines) - 1:
                self.cy += 1
                self.cx = 0

        # Snap cursor to end of line if we moved vertically to a shorter line
        new_row_len = len(self.lines[self.cy])
        if self.cx > new_row_len:
            self.cx = new_row_len

    def handle_editing(self, key: int):
        """Handles text insertion, deletion, and newlines."""
        line = self.lines[self.cy]

        # Enter / Newline
        if key in (10, 13):
            self.lines.insert(self.cy + 1, line[self.cx:])
            self.lines[self.cy] = line[:self.cx]
            self.cy += 1
            self.cx = 0
            self.is_modified = True

        # Backspace
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if self.cx > 0:
                self.lines[self.cy] = line[:self.cx - 1] + line[self.cx:]
                self.cx -= 1
                self.is_modified = True
            elif self.cy > 0:
                # Merge with previous line
                prev_line = self.lines.pop(self.cy)
                self.cy -= 1
                self.cx = len(self.lines[self.cy])
                self.lines[self.cy] += prev_line
                self.is_modified = True

        # Regular typing
        elif 32 <= key <= 126:
            char = chr(key)
            self.lines[self.cy] = line[:self.cx] + char + line[self.cx:]
            self.cx += 1
            self.is_modified = True

    def get_syntax_segments(self, line: str) -> List[Tuple[str, int]]:
        """
        Parses a line and returns a list of (text, color_pair_index) tuples.
        """
        segments = []
        last_pos = 0

        # Search for all matches in the line
        for match in self.syntax_regex.finditer(line):
            start, end = match.span()

            # Add normal text before the match
            if start > last_pos:
                segments.append((line[last_pos:start], 0))

            # Determine color based on the named group of the match
            kind = match.lastgroup
            if kind == 'KEYWORD':
                color = 3
            elif kind == 'STRING':
                color = 4
            elif kind == 'COMMENT':
                color = 5
            elif kind == 'NUMBER':
                color = 6
            else:
                color = 0

            segments.append((line[start:end], color))
            last_pos = end

        # Add remaining text after the last match
        if last_pos < len(line):
            segments.append((line[last_pos:], 0))

        return segments

    def render(self):
        """Draws the editor interface."""
        self.stdscr.erase()
        self.height, self.width = self.stdscr.getmaxyx()

        # Calculate margins
        self.line_num_width = len(str(len(self.lines))) + 2
        view_height = self.height - 1  # Reserve 1 line for status bar
        view_width = self.width - self.line_num_width

        # Adjust scroll if cursor is out of view
        if self.cy < self.scroll_y:
            self.scroll_y = self.cy
        elif self.cy >= self.scroll_y + view_height:
            self.scroll_y = self.cy - view_height + 1

        # Draw Visible Lines
        for i in range(view_height):
            file_idx = i + self.scroll_y
            if file_idx >= len(self.lines):
                break

            # Draw Line Number
            line_num = str(file_idx + 1).rjust(self.line_num_width - 1)
            self.stdscr.attron(curses.color_pair(2))
            self.stdscr.addstr(i, 0, f"{line_num} ")
            self.stdscr.attroff(curses.color_pair(2))

            # Draw Content with Syntax Highlighting
            line_content = self.lines[file_idx][:view_width]

            current_x = self.line_num_width
            segments = self.get_syntax_segments(line_content)

            for text, color_idx in segments:
                # Truncate text if it goes beyond view width
                # This simple logic relies on view_width being handled by slicing line_content earlier
                # But since segments might overflow if not handled carefully, we print sequentially.
                # Given line_content is already sliced, segments will sum up to line_content.

                if color_idx > 0:
                    self.stdscr.attron(curses.color_pair(color_idx))
                    self.stdscr.addstr(i, current_x, text)
                    self.stdscr.attroff(curses.color_pair(color_idx))
                else:
                    self.stdscr.addstr(i, current_x, text)
                current_x += len(text)

        # Draw Status Bar
        mod_char = "*" if self.is_modified else " "
        status = f" {self.filename}{mod_char} | Ln {self.cy+1}, Col {self.cx+1} | ^S: Save | ^Q: Quit "

        self.stdscr.attron(curses.color_pair(1))
        try:
            self.stdscr.addstr(self.height - 1, 0, status.ljust(self.width))
        except curses.error:
            pass  # Ignore edge case
        self.stdscr.attroff(curses.color_pair(1))

        # Position Cursor
        screen_y = self.cy - self.scroll_y
        screen_x = self.cx + self.line_num_width

        # Ensure cursor stays on screen (safety check)
        if 0 <= screen_y < view_height and 0 <= screen_x < self.width:
            self.stdscr.move(screen_y, screen_x)

        self.stdscr.refresh()

    def run(self):
        """Main event loop."""
        curses.raw()
        self.stdscr.nodelay(False)

        while self.running:
            self.render()
            key = self.stdscr.getch()

            # Quit (Ctrl + Q)
            if key == 17:
                if self.is_modified:
                    response = self.get_input(
                        "Unsaved changes! Quit anyway? (y/n): ")
                    if response and response.lower() == 'y':
                        self.running = False
                else:
                    self.running = False

            # Save (Ctrl + S)
            elif key == 19:
                if not self.filename or self.filename == "untitled.txt":
                    new_name = self.get_input("Save As: ", self.filename)
                    if new_name:
                        self.filename = new_name
                        self.save_file()
                else:
                    self.save_file()

            # Navigation
            elif key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT,
                         curses.KEY_RIGHT):
                self.handle_navigation(key)

            # Editing
            else:
                self.handle_editing(key)


def main(stdscr):
    filename = sys.argv[1] if len(sys.argv) > 1 else "untitled.txt"
    editor = TextEditor(stdscr, filename)
    editor.run()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass
