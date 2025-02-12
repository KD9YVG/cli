class command:
    def split(command):
        # Split the string into a list of words
        words = command.split()
    
        # Get the first word
        first_word = words[0] if words else ""
    
        # Get the remaining words (if any)
        remaining_words = words[1:] if len(words) > 1 else []
    
        return first_word, remaining_words

    def command(command):
        # Split the string into a list of words
        words = command.split()
    
        # Get the first word
        first_word = words[0] if words else ""

        return first_word

    def arguments(command):
        # Split the string into a list of words
        words = command.split()

        # Get the remaining words (if any)
        remaining_words = words[1:] if len(words) > 1 else []

        return remaining_words


# instir = input("Enter a command: ")
# print(str(command.split(instir)))
# print(str(command.command(instir)))
# print(str(command.arguments(instir)))