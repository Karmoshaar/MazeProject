from .cell import Cell

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    def get_neighbors(self, cell):
        neighbors = []
        r, c = cell.row, cell.col

        if not cell.walls["top"] and r > 0:
            neighbors.append(self.grid[r - 1][c])
        if not cell.walls["right"] and c < self.cols - 1:
            neighbors.append(self.grid[r][c + 1])
        if not cell.walls["bottom"] and r < self.rows - 1:
            neighbors.append(self.grid[r + 1][c])
        if not cell.walls["left"] and c > 0:
            neighbors.append(self.grid[r][c - 1])

        return neighbors
