import util
import engine
import ui
from termcolor import colored

LEVEL_NAME = "Maps\\TestMap.txt"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
map = engine.create_board(LEVEL_NAME)

# def color_map(bcolors, map):
#     walls_and_doors = ["/", "\\", "-", "+", "|"]
#     for element in map:
#         if element == "H":
#             element = f"{bcolors.OKGREEN}H"
#         if element == "F":
#             element = f"{bcolors.OKBLUE}F"
#         if element in walls_and_doors:
#             element = f"{bcolors.WARNING}{element}"
#     return map

def display_board(board = list()):
    for row in board:
        for col in row:
            print(f"{bcolors.WARNING}{col}", end="")
        print()
