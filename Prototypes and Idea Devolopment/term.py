from blessed import Terminal

def main():
    term = Terminal()
    
    print(term.clear)  # Clear the screen
    print(term.bold_blue("Welcome to the Blessed Demo!"))
    
    with term.location(5, 5):  # Move cursor to (column 5, row 5)
        print(term.green_on_black("This text is green on black!"))
    
    with term.location(10, 7):
        print(term.bold_red("Press any key to continue..."))
        print(term.blink("Press ESC to exit."))
    
    with term.cbreak():  # Enable immediate key reading
        key = term.inkey()
        
        if key.name == "KEY_ESCAPE":
            print(term.clear)
            print(term.red("You pressed ESC. Exiting..."))
        else:
            print(term.clear)
            print(term.bold_yellow(f"You pressed: {key}"))
    
    print(term.bold("\nThanks for using Blessed!"))

if __name__ == "__main__":
    main()
