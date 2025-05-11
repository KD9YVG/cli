import blessed
import sys

term = blessed.Terminal()

## Define starting parameters
if sys.argv[1]:
    path = sys.argv[1]
else:
    path = 'null.null_null'

class Text:
    def __init__(self):
        print(term.fullscreen())
        if path != "null.null_null":
            open(path, 'r+')
        else:
            open('null.null_null', 'w+')
        print(term.clear)
        print(term.center(term.on_white(term.black('pyText 0.0.1 Alpha'))))
        print(term.move_down)
    def setModeWrite(mode):
        ## This checks permissions and if possible sets the mode to write
        print("THERE ARE BLOODY TEST THINGS EVERYWHERE!")
    try:
        print('THIS IS TEMPORARY')
    except:
        print("OH DEAR GOODNESS ME!")

try:
    Text()
except KeyboardInterrupt:
    print(term.exit_fullscreen())
    exit(0)