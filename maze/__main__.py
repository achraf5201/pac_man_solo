from maze.maze_view import MazeView
import arcade


def main():
    window = arcade.Window(fullscreen=True, title="Maze")

    view = MazeView()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
