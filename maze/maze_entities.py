import random
import arcade
from maze.maze_adapter import MazeAdapter


class Entity:
    pass


class Player:
    def __init__(self, x, y, pixel_x, pixel_y, speed, maze, cell_size):
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        self.cell_x = x
        self.cell_y = y
        self.speed = speed
        self.maze_model = MazeAdapter(maze)
        self.dir = None
        self.next_dir = None

    def hundle_input(self, dir):
        self.next_dir = dir

    def get_cor(self, dir):
        if dir == 1:
            return 0, -1
        elif dir == 2:
            return 1, 0
        elif dir == 4:
            return 0, 1
        elif dir == 8:
            return -1, 0

    def update(self):
        if self.maze_model.can_move(self.cell_x, self.cell_y, self.next_dir):
            x, y = self.get_cor(self.next_dir)
            self.cell_x = x
            self.cell_y


class Ghost(Entity):
    pass


class EntityManager:
    pass
