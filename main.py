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
winner_board = "Maps\\Winner_text.txt"

'''
def create_player():
   
    pass
'''



def main():
    map = engine.create_board(LEVEL_NAME)
    player = Golum(20, 'Gollum', '@')
    enemy_list = lokking_for_enemy(map)
    #enemy_list = []
    while enemy_list:
        time.sleep(0.02)
        os.system('cls')
        ui.display_screen(map, enemy_list, player)
        map, enemy_list = player.player_move(map, enemy_list)
        map = enemys_move(map, enemy_list)
        if player.is_game_over():
            break
    if not enemy_list and not player.is_game_over():
        os.system('cls')
        winner = engine.create_winner_board(winner_board)
        ui.display_screen(winner, enemy_list, player = player)
    elif player.is_game_over():
        os.system('cls') 

        #coś tam do wyświetlenia

        #ui.display_screen(map, enemy_list, player)
       
    
        

def lokking_for_enemy(map):
    enemy_list = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == "H":
                enemy_list.append(Hobbit([row, col], "Hobbit", map[row][col]))
            elif map[row][col]  == "B":
                enemy_list.append(Bumbur([row, col], "Bumbur", map[row][col]))
    return enemy_list

def enemys_move(map, enemy_list):
    if len(enemy_list) > 0:
        for enemy in enemy_list:

            map = enemy.move(map)
    return map

if __name__ == '__main__':
    main()
