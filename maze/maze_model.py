from mazegenerator import MazeGenerator


class MazeModel:
    def __init__(self, maze):
        self.walls = maze._maze

        self.height = len(self.walls)
        self.width = len(self.walls[0])

        self.corners = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
        ]

        self.center = (self.width // 2, self.height // 2)

    def has_wall(self, x, y, deriction):
        return self.walls[y][x] & deriction != 0

    def can_move(self, x, y, deriction):
        return self.walls[y][x] & deriction == 0

    def neighbors(self, x, y):
        res = []
        if 0 <= x < self.width and 0 <= y - 1 < self.height:
            if self.can_move(x, y, 1):
                res.append((x, y - 1))
        if 0 <= x + 1 < self.width and 0 <= y < self.height:
            if self.can_move(x, y, 2):
                res.append((x + 1, y))
        if 0 <= x < self.width and 0 <= y + 1 < self.height:
            if self.can_move(x, y, 4):
                res.append((x, y + 1))
        if 0 <= x - 1 < self.width and 0 <= y < self.height:
            if self.can_move(x, y, 8):
                res.append((x - 1, y))
        return res


# m = MazeModel(
#     MazeGenerator(size=(30, 17), entry_cell=(0, 0), exit_cell=(15, 15))
# )
# print(m.neighbors(0, 0))


# # MazeModel
# # │
# # ├── walls
# # ├── width
# # ├── height
# # ├── corners
# # ├── center
# # └── methods
# #     ├── has_wall()
# #     ├── can_move()
# #     └── neighbors()
