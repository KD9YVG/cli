import blessed
import time

term = blessed.Terminal()

class Text:
    def __init__(self):
        print(term.enter_fullscreen())
        print(term.clear)
        print(term.on_white(term.black('pyText 0.0.1 Alpha')))
        print(term.move_down)
        print(term.move_xy(0, term.height - 1) + term.on_white(term.black('Ctrl+X - Close    Ctrl+S - Save')))

if __name__ == "__main__":
    try:
        Text()
    finally:
        time.sleep(2)
        print(term.exit_fullscreen())