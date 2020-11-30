from Global import *

class Hobbit(Global_class):
    
    def __init__(self, postion, name, icon):
        self.current_position = postion
        self.name = name
        self.icon = icon
        self.curent_icon = " "
        self.curent_direction = ""
        self.step_count = 0
        self.barrier = ["/", "\\", "|", "-", "+"]
    
    def move(self, map):
        if self.curent_direction == "" and self.step_count == 0:
            self.step_count, self.curent_direction = self.get_move_data()
        if self.get_new_position_icon(map, self.curent_direction) == " ":
            map = self.make_move(map, self.curent_direction, self.step_count)
        elif self.get_new_position_icon(map, self.curent_direction) in self.barrier:
            self.curent_direction = ""
            self.step_count = 0
        return map

    def make_move(self, map, direction, step):
        new_position = self.next_position(direction)
        map[self.current_position[0]][self.current_position[1]] = self.curent_icon
        self.current_position = new_position
        map[new_position[0]][new_position[1]] = self.icon
        self.step_count -= 1
        if self.step_count <= 0:
            self.curent_direction = ""
            self.step_count = 0
        return map
    
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

    def get_move_data(self):
        directions = ["LEFT","RIGHT","UP","DOWN"]
        direction = directions[random.randint(0, len(directions) - 1)]
        step = random.randint(0, 4)
        return step, direction
    
    def get_new_position_icon(self, map, letter):
        if letter == 'UP':
            return map[self.current_position[0] - 1][self.current_position[1]]
        elif letter == 'DOWN':
            return map[self.current_position[0] + 1][self.current_position[1]]
        elif letter == "LEFT":
            return map[self.current_position[0]][self.current_position[1] - 1]
        elif letter == 'RIGHT':
            return map[self.current_position[0]][self.current_position[1] + 1]

