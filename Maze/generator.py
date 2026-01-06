import random

class MazeGenerator:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()

    def generate(self, r=0, c=0):
        cell = self.maze.grid[r][c]
        self.visited.add(cell)

        directions = ["top", "right", "bottom", "left"]
        random.shuffle(directions)

        for d in directions:
            nr, nc = r, c
            if d == "top": nr -= 1
            if d == "right": nc += 1
            if d == "bottom": nr += 1
            if d == "left": nc -= 1

            if 0 <= nr < self.maze.rows and 0 <= nc < self.maze.cols:
                neighbor = self.maze.grid[nr][nc]
                if neighbor not in self.visited:
                    cell.walls[d] = False
                    opposite = {
                        "top": "bottom",
                        "right": "left",
                        "bottom": "top",
                        "left": "right"
                    }
                    neighbor.walls[opposite[d]] = False
                    self.generate(nr, nc)
