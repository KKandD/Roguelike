import msvcrt
import time


def if_button_pressed():   
    if msvcrt.kbhit():
        possible_letter_choice = [b'w', b's', b'a', b'd']
        key = msvcrt.getch()
        if key not in possible_letter_choice:
            return False
        else:
            return key

def get_keyboard_letter():
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

while True:
    time.sleep(0.5)
    print(get_keyboard_letter())






# import msvcrt

# if msvcrt.kbhit():
#     possible_letter_choice = [b'w', b's', b'a', b'd']
#     key = msvcrt.getch()
#     if key not in possible_letter_choice:
#         continue
#     else:
#         if key == b'w':
#             letter = 'UP'
#         elif key == b's':
#             letter = 'DOWN'
#         elif key == b'a':
#             letter = 'LEFT'
#         elif key == b'd':
#             letter = 'RIGHT'
#         #key_not_pressed = not key_not_pressed
#         print(letter)



# letter = get_keyboard_letter()

# print(letter)
