import blessed

term = blessed.Terminal()

class Text:
    def __init__(self):
        print(term.center(term.on_white(term.black('pyText 0.0.1 Alpha'))))
        print(term.move_down)

Text()