import os
import random

class Global_class:

    @staticmethod
    def get_file_path(file_name):# Method which get file path
        file_dir = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(file_dir, file_name)
        return my_file

class Player():

    def __init__(self, hit_count, name, icon):
        self.hit_count = hit_count
        self.name = name
        self.icon = icon
        
    def player_move(self):
        pass

    def fight_randomness(self):
        hit_or_not = ['H', 'H', 'H', 'H', 'L']
        random_result = random.choice(hit_or_not)
        return random_result
    
    def pick_fish(self):
        self.hit_count += 2

    def print_player_parameters(self):
        print(f'Player name {self.name}\nHit_count {self.hit_count}\nIcon {self.icon}' )