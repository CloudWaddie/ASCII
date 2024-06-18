def generate_letter_ascii_art(word):
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
        'Q': "  ___  \n / _ \\ \n| | | |\n| |_| |\n \\__\\_\\",
        'R': " ____  \n|  _ \\ \n| |_) |\n|  _ < \n|_| \\_\\",
        'S': " ____  \n/ ___| \n\\___ \\ \n ___) |\n|____/ ",
        'T': " _____ \n|_   _|\n  | |  \n  | |  \n  |_|  ",
        'U': " _   _ \n| | | |\n| | | |\n| |_| |\n \\___/ ",
        'V': "__     __\n\\ \\   / /\n \\ \\ / / \n  \\ V /  \n   \\_/   ",
        'W':
        "__        __\n\\ \\      / /\n \\ \\ /\\ / / \n  \\ V  V /  \n   \\_/\\_/   ",
        'X': "__  __\n\\ \\/ /\n \\  / \n /  \\ \n/_/\\_\\",
        'Y': "__   __\n\\ \\ / /\n \\ V / \n  | |  \n  |_|  ",
        'Z': " _____\n|__  /\n  / / \n / /_ \n/____|"
    }

    word = word.upper()

    output = ""
    for letter in word:
        if letter not in letter_patterns:
            return "Invalid letter."
        output = output + "\n" + letter_patterns[letter]
    return output


word = "ZS"
print(generate_letter_ascii_art(word))
