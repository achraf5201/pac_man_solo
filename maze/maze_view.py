import arcade
from maze.maze_adapter import MazeAdapter
from mazegenerator import MazeGenerator


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.maze_g = MazeGenerator(
            size=(38, 20), entry_cell=(0, 0), exit_cell=(15, 15)
        )
        self.maze_adapter = MazeAdapter(self.maze_g, cell_size=50)

        self.maze_adapter._calc_config()

    def on_draw(self):
        self.clear()
        for row_index, row in enumerate(self.maze_adapter.walls):
            for col_index, cell_value in enumerate(row):
                x, y = self.maze_adapter.cell_to_pixel(col_index, row_index)
                self.maze_adapter._render_maze(cell_value, x, y)
        self.maze_adapter._render_hud()
