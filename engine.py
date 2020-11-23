from Global import *

def create_board(level_name):
    map_path = Global_class.get_file_path(level_name)
    with open(map_path,"r") as file:
        file_text = file.read().split("\n")
        for row in range(len(file_text)):
            file_text[row] = list(file_text[row])
        return file_text
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
