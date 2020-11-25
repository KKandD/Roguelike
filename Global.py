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
        self.current_position = [0, 0]

    def if_button_pressed(self):
        possible_letter_choice = [b'w', b's', b'a', b'd']
        if msvcrt.kbhit() and msvcrt.getch() in possible_letter_choice:
            return msvcrt.getch()
        else:
            return False

    def get_keyboard_letter(self):
        letter = ''
        key = if_button_pressed()
        if key:
            if key == b'w':
                letter = 'UP'
            elif key == b's':
                letter = 'DOWN'
            elif key == b'a':
                letter = 'LEFT'
            elif key == b'd':
                letter = 'RIGHT'

            return letter
        else:
            return None



    def is_move_valid(self):

        return True

    def check_enviroment(self, map, letter):
        #check directions
        if letter == 'UP':
            return map[self.current_position[0] - 1][self.current_position[1]] # tu otrzymamy [[row], [col]] 
        elif letter == 'DOWN':
            return map[self.current_position[0] + 1][self.current_position[1]]
        elif letter == "LEFT":
            return map[self.current_position[0]][self.current_position[1] - 1]
        elif letter == 'RIGHT':
            return map[self.current_position[0]][self.current_position[1] + 1]
            

    def player_move(self):

        letter = self.is_move_valid()
        if letter:
            
            pass

    def fight_randomness(self):
        hit_or_not = ['H', 'H', 'H', 'H', 'L']
        random_result = random.choice(hit_or_not)
        return random_result

    def is_game_over(self):
        if self.hit_count <= 0:
            return True

    def is_fight(self, opponent, hit_count):
        fight_result = Player.fight_randomness(self)
        while fight_result == 'L':
            if opponent == 'hobbit':
                self.hit_count -= 1
            elif opponent =='bombur':
                self.hit_count -= 4
            if self.hit_count == 0:
                break
            else:
                fight_result = Player.fight_randomness(self)
                continue
        if fight_result == 'H':
            if opponent == 'hobbit':
                self.hit_count -= 1
            else:
                self.hit_count -= 4
    
    def pick_fish(self):
        self.hit_count += 2

    def print_player_parameters(self):
        print(f'Player name {self.name}\nHit_count {self.hit_count}\nIcon {self.icon}' )

class Opponent(Player):

    def __init__(self, strike_to_kill, name, icon):
        super().__init__(Opponent, name, icon)
        self.strike_to_kill = strike_to_kill