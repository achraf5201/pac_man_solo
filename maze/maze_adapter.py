import arcade
import sys
import time


class MazeAdapter:
    def __init__(self, maze, cell_size=60):
        self.maze = maze
        self.maze_width = 0
        self.maze_height = 0
        self.screen_width = 0
        self.screen_height = 0
        self.cell_size = cell_size
        self.offset_x = 0
        self.offset_y = 0

    def grid_to_pixel(self, row, col):
        x = self.offset_x + (col * self.cell_size) + self.cell_size / 2
        y = self.offset_y + (row * self.cell_size) + self.cell_size / 2
        return x, y

    def _calc_config(self):
        self.maze_width = len(self.maze._maze[0])
        self.maze_height = len(self.maze._maze)

        width = self.maze_width * self.cell_size
        height = self.maze_height * self.cell_size

        self.screen_width, self.screen_height = arcade.get_display_size()
        if width >= self.screen_width or height >= self.screen_height:
            print("width > self.screen_width or height > self.screen_height")
            sys.exit()

        self.offset_x = (
            self.screen_width - (self.maze_width * self.cell_size)
        ) / 2
        self.offset_y = (
            self.screen_height - (self.maze_height * self.cell_size)
        ) / 2

    def _render_maze(self, cell_value, x, y):
        if cell_value == 15:
            arcade.draw_lbwh_rectangle_filled(
                x, y, self.cell_size, self.cell_size, arcade.color.WHITE
            )

        if cell_value & 1:
            arcade.draw_lbwh_rectangle_filled(
                x, y + self.cell_size, self.cell_size, 2, arcade.color.WHITE
            )

        if cell_value & 2:
            arcade.draw_lbwh_rectangle_filled(
                x + self.cell_size, y, 2, self.cell_size, arcade.color.WHITE
            )

        if cell_value & 4:
            arcade.draw_lbwh_rectangle_filled(
                x, y, self.cell_size, 2, arcade.color.WHITE
            )

        if cell_value & 8:
            arcade.draw_lbwh_rectangle_filled(
                x, y, 2, self.cell_size, arcade.color.WHITE
            )
