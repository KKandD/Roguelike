import util
import engine
import ui
import time
from Global import *
from Player import *
from Enemy import *

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

LEVEL_NAME = "Maps\\TestMap.txt"

'''
def create_player():
   
    pass
'''



def main():
    map = engine.create_board(LEVEL_NAME)
    player = Golum(8, 'Gollum', '@')
    
    while True:
        time.sleep(0.0)
        os.system('cls')
        ui.display_screen(map, player)
        map = player.player_move(map)
        enemy_list = lokking_for_enemy(map)
        map = enemys_move(map, enemy_list)

def lokking_for_enemy(map):
    enemy_list = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == "H":
                enemy_list.append(Hobbit([row, col], "Hobbit", map[row][col]))
    return enemy_list

def enemys_move(map, enemy_list):
    if len(enemy_list) > 0:
        for enemy in enemy_list:

            map = enemy.move(map)
    return map

if __name__ == '__main__':
    main()
