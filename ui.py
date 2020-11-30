from Global import *

def display_screen(board, player):

    for row in board:
        for col in row:
            print(col, end="")
        print()
    print_player_data(player.name, player.current_position, player.hit_count, player.score)


def print_player_data(name = "Player", position = [0,0], hit_count = 0, score = 0):
    information_text = f"| Player name: {name} | {name} hit count: {hit_count} | {name} score: {score} | {name} position: {position} |"
    print("-" * len(information_text) + "\n" + information_text + "\n" + "-" * len(information_text))

