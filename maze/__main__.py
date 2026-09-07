from maze.maze_model import MazeModel
import arcade


def main():
    window = arcade.Window(fullscreen=True, title="Maze")

    view = MazeModel()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
