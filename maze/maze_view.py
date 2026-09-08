import arcade
from maze.maze_adapter import MazeAdapter
from mazegenerator import MazeGenerator
from ghosts.ghosts import Ghosts


class MazeView(arcade.View):
    def __init__(self):
        super().__init__()
        self.maze_g = MazeGenerator(
            size=(30, 17), entry_cell=(0, 0), exit_cell=(15, 15)
        )
        self.maze_adapter = MazeAdapter(self.maze_g, cell_size=60)

        self.maze_adapter._calc_config()
        self.ghosts = Ghosts(self.maze_g)

    def on_draw(self):
        self.clear()
        for row_index, row in enumerate(self.maze_adapter.maze._maze):
            for col_index, cell_value in enumerate(row):
                x = self.maze_adapter.offset_x + (
                    col_index * self.maze_adapter.cell_size
                )
                y = self.maze_adapter.offset_y + (
                    (self.maze_adapter.maze_height - 1 - row_index)
                    * self.maze_adapter.cell_size
                )

                self.maze_adapter._render_maze(cell_value, x, y)
