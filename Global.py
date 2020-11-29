import os
import random
import msvcrt
import keyboard
import arcade

class Global_class:

    @staticmethod
    def get_file_path(file_name):# Method which get file path
        file_dir = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(file_dir, file_name)
        return my_file

class Items():
    def __init__(self, fish_count, chapel_count):
        self.fish_count = fish_count
        self.chapel_count = chapel_count
        self.dictionary = {'F' : fish_count, 'C' : chapel_count}

    
        

class Player():

    def __init__(self, hit_count, name, icon):
        self.hit_count = hit_count
        self.name = name
        self.icon = icon
        self.current_position = [1, 1]
        self.current_icon = ' '
        self.walk_sound = arcade.load_sound("sounds/footstep3.ogg")
        self.eat_sound = arcade.load_sound("sounds/eating_fish.ogg")
        self.door_sound = arcade.load_sound("sounds/door_opening2.ogg")

    def if_button_pressed(self):   
        if msvcrt.kbhit():
            possible_letter_choice = [b'w', b's', b'a', b'd']
            key = msvcrt.getch()
            if key not in possible_letter_choice:
                return False
            else:
                return key

    def get_keyboard_letter(self):
        letter = ''
        key = self.if_button_pressed()
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


    def is_move_valid(self, letter):
        forbidden_list = ['+', '-', '|']
        if letter not in forbidden_list:
            return True
        else:
            return False

    def get_new_position_icon(self, map, letter):
        if letter == 'UP':
            return map[self.current_position[0] - 1][self.current_position[1]]
        elif letter == 'DOWN':
            return map[self.current_position[0] + 1][self.current_position[1]]
        elif letter == "LEFT":
            return map[self.current_position[0]][self.current_position[1] - 1]
        elif letter == 'RIGHT':
            return map[self.current_position[0]][self.current_position[1] + 1]

    def next_position(self, letter):
        new_position = []
        if letter == 'UP':
            new_position = [self.current_position[0] - 1, self.current_position[1]]
        elif letter == 'DOWN':
            new_position = [self.current_position[0] + 1, self.current_position[1]]
        elif letter == "LEFT":
            new_position = [self.current_position[0], self.current_position[1] - 1]
        elif letter == 'RIGHT':
            new_position = [self.current_position[0], self.current_position[1] + 1]
        return new_position # [1, 1]

    def check_for_item(self, icon):
        self.current_icon = icon
        if self.current_icon == 'F' and self.hit_count == 10:
            return self.current_icon
        elif self.current_icon == 'F' and self.hit_count < 10:
            self.pick_fish()
            return ' '       
        if self.current_icon == '/' or self.current_icon == '\\':
            self.door_sound.play()
            return self.current_icon
        else:
            return ' '


    def player_move(self, map): 
        letter = self.get_keyboard_letter()
        next_field_icon = self.get_new_position_icon(map, letter)
        if letter and self.is_move_valid(next_field_icon):
            new_position = self.next_position(letter)
            map[self.current_position[0]][self.current_position[1]] = self.current_icon 
            self.current_icon = self.check_for_item(next_field_icon)
            self.current_position = new_position
            self.walk_sound.play()
            map[new_position[0]][new_position[1]] = self.icon 
        return map 

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
        self.hit_count += 1
        self.eat_sound.play()


    def print_player_parameters(self):
        print(f'Player name {self.name}\nHit_count {self.hit_count}\nIcon {self.icon}' )

class Opponent(Player):

    def __init__(self, strike_to_kill, name, icon):
        super().__init__(Opponent, name, icon)
        self.strike_to_kill = strike_to_kill