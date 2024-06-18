def generate_letter_ascii_art(letter):
    letter_patterns = {
        'A': "    _    \n   / \\   \n  / _ \\  \n / ___ \\ \n/_/   \\_\\",
        'B': "____  \n| __) \n|  _ \\ \n| |_) |\n|____/ ",
        'C': "  ____ \n / ___|\n| |    \n| |___ \n \\____|",
        'D': " ____  \n|  _ \\ \n| | | |\n| |_| |\n|____/ ",
        'E': " _____ \n| ____|\n|  _|  \n| |___ \n|_____|",
        'F': " _____ \n|  ___|\n| |_   \n|  _|  \n|_|   ",
        'G': "  ____ \n / ___|\n| |  _ \n| |_| |\n \\____/",
        'H': " _   _ \n| | | |\n| |_| |\n|  _  |\n|_| |_|",
        'I': " ___ \n|_ _|\n | | \n | | \n|___|",
        'J': "     _ \n    | |\n _  | |\n| |_| |\n \\___/ ",
        'K': " _  __\n| |/ / \n| ' /  \n| . \\  \n|_|\\_\\",
        'L': " _     \n| |    \n| |    \n| |___ \n|_____|",
        'M': " __  __ \n|  \\/  |\n| |\\/| |\n| |  | |\n|_|  |_|",
        'N': " _   _ \n| \\ | |\n|  \\| |\n| |\\  |\n|_| \\_|",
        'O': "  ___  \n / _ \\ \n| | | |\n| |_| |\n \\___/ ",
        'P': " ____  \n|  _ \\ \n| |_) |\n|  __/ \n|_|    ",
        'Z': "#### \n   # \n  #  \n #   \n#### "
    }

    letter = letter.upper()
    if letter not in letter_patterns:
        return "Invalid letter."

    return letter_patterns[letter]

letter = "P"
print(generate_letter_ascii_art(letter))
