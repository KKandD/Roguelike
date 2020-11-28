import keyboard
import time

def if_button_pressed():
        possible_letter_choice = ['w', 'a', 's', 'd']
        key = keyboard.get_hotkey_name()
        if key in possible_letter_choice:
            return key
        else:
            return False

def get_keyboard_letter():
    letter = ''
    key = if_button_pressed()
    if key:
        if key == 'w':
            letter = 'UP'
        elif key == 's':
            letter = 'DOWN'
        elif key == 'a':
            letter = 'LEFT'
        elif key == 'd':
            letter = 'RIGHT'
        return letter
    else:
        return None

while True:
    letter = get_keyboard_letter()
    if letter:
        print(letter)
    time.sleep(0.2)

