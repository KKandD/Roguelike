import util
import engine
import ui
import time
from Global import *

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

LEVEL_NAME = "Maps\\TestMap.txt"

'''
def create_player():
   
    pass
'''



def main():
    #player = create_player()
    map = engine.create_board(LEVEL_NAME)
    player = Player(9, 'Gollum', '@')
    #ui.display_board(board)
    while True:

        time.sleep(0.4)
        os.system('cls')
        ui.display_board(map)
        map = player.player_move(map)

    """ util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen() """


if __name__ == '__main__':
    main()
