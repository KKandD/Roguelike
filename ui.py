from Global import *

def display_screen(board, player):
    walls_and_doors = {
        "/": Style.font_yellow + "/" + Style.reset,
        "\\": Style.font_yellow + "\\" + Style.reset,
        "-": Style.Background_red + " " + Style.reset,
        "+": Style.Background_red + " " + Style.reset,
        "|": Style.Background_red + " " + Style.reset,
        "@": Style.font_cyan + "@" + Style.reset,
        "H": Style.font_green + "H" + Style.reset,
        "F": Style.font_blue + "F" + Style.reset,
        " ": " ",
        }

    for row in board:
        for col in row:
            #print(walls_and_doors[col], end="")
            print(col, end="")
        print()
    print_player_data(player.name, player.current_position, player.hit_count, player.score)


def print_player_data(name = "Player", position = [0,0], hit_count = 0, score = 0, key = 0):
    information_text = f"| Player name: {name} | {name} hit count: {hit_count} | {name} score: {score} | {name} position: {position} | key: {key} |"
    print("-" * len(information_text) + "\n" + information_text + "\n" + "-" * len(information_text))

class Style():
    font_black = '\033[30m'
    font_purple = '\033[95m'
    font_blue = '\033[94m'
    font_cyan = '\033[96m'
    font_green = '\033[92m'
    font_yellow = '\033[93m'
    font_red = '\033[91m'
    font_white = '\033[0m'
    font_bold = '\033[1m'
    reset = '\u001b[0m'
    font_underline = '\033[4m'
    Background_black        = "\033[40m"
    Background_red          = "\033[41m"
    Background_green        = "\033[42m"
    Background_yellow       = "\033[43m"
    Background_blue         = "\033[44m"
    Background_magenta      = "\033[45m"
    Background_cyan         = "\033[46m"
    Background_lightGray    = "\033[47m"
    Background_darkGray     = "\033[100m"
    Background_lightRed     = "\033[101m"
    Background_lightGreen   = "\033[102m"
    Background_lightYellow  = "\033[103m"
    Background_lightBlue    = "\033[104m"
    Background_lightMagenta = "\033[105m"
    Background_lightCyan    = "\033[106m"
    Background_white        = "\033[107m"