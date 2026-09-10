import arcade
from maze.maze_adapter import MazeAdapter
from mazegenerator import MazeGenerator
from enum import Enum
from maze.maze_entities import Player


class GameView(arcade.View):
    def __init__(self, cell_size=50):
        super().__init__()
        self.maze_g = MazeGenerator(
            size=(38, 20), entry_cell=(0, 0), exit_cell=(15, 15)
        )
        self.maze_adapter = MazeAdapter(self.maze_g, cell_size)

        self.maze_adapter._calc_config()
        self.cell_size = cell_size
        c_x, c_y = self.maze_adapter.center
        p_x, p_y = self.maze_adapter.cell_to_pixel(c_x, c_y)
        self.player = Player(c_x, c_y, p_x, p_y, 20, self.maze_g, cell_size)

    def on_draw(self):
        self.clear()
        for row_index, row in enumerate(self.maze_adapter.walls):
            for col_index, cell_value in enumerate(row):
                x, y = self.maze_adapter.cell_to_pixel(col_index, row_index)
                self.maze_adapter._render_maze(cell_value, x, y)
        # self.maze_adapter._render_hud()
        if self.maze_adapter.walls[self.player.cell_y][self.player.cell_x] == 15:
            cord = self.maze_adapter.p_neighbors(
                self.player.cell_x, self.player.cell_y
            )

            for c in cord:
                x, y = c
                if (
                    self.maze_adapter.walls[y][x]
                    != 15
                ):
                    self.player.cell_x = x
                    self.player.cell_y = y
                    px, py = self.maze_adapter.cell_to_pixel(x, y)
                    self.player.pixel_x = px
                    self.player.pixel_y = py
        arcade.draw_circle_filled(
            self.player.pixel_x + self.cell_size / 2,
            self.player.pixel_y + self.cell_size / 2,
            10,
            arcade.color.RED,
        )

    def on_update(self, delta_time):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.next_dir = 1
        elif symbol == arcade.key.DOWN:
            self.next_dir = 4
        elif symbol == arcade.key.LEFT:
            self.next_dir = 2
        elif symbol == arcade.key.RIGHT:
            self.next_dir = 8

        elif symbol == arcade.key.W:
            self.next_dir = 1
        elif symbol == arcade.key.S:
            self.next_dir = 4
        elif symbol == arcade.key.A:
            self.next_dir = 2
        elif symbol == arcade.key.D:
            self.next_dir = 8
