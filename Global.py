import os
import random
import msvcrt
import keyboard
import arcade
import time

class Global_class:

    DATA_WIGHT = 15

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
 



