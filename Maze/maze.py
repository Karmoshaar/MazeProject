"""
Maze grid and helpers.
Creates grid of cells, provides start and end,
and links neighbors according to removed walls.
"""
from typing import List, Optional, Tuple
from .cell import Cell

class Maze:
    def __init__(self, rows: int, cols: int, start: Tuple[int,int]=None, end: Tuple[int,int]=None):
        if rows < 1 or cols < 1:
            raise ValueError("rows and cols must be >= 1")
        self.rows = rows
        self.cols = cols
        self.grid: List[List[Cell]] = [
            [Cell(r, c) for c in range(cols)] for r in range(rows)
        ]
        # default start top-left, end bottom-right
        self.start: Cell = self.grid[0][0] if start is None else self.cell_at(*start)
        self.end: Cell = self.grid[rows - 1][cols - 1] if end is None else self.cell_at(*end)

    def cell_at(self, row: int, col: int) -> Cell:
        return self.grid[row][col]

    def neighbors_positions(self, cell: Cell):
        r, c = cell.row, cell.col
        positions = []
        if r > 0:
            positions.append(("top", (r - 1, c)))
        if c < self.cols - 1:
            positions.append(("right", (r, c + 1)))
        if r < self.rows - 1:
            positions.append(("bottom", (r + 1, c)))
        if c > 0:
            positions.append(("left", (r, c - 1)))
        return positions

    def link_neighbors(self):
        """
        Populate each cell's neighbors list with adjacent cells that are reachable
        (i.e., there is no wall between them).
        """
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                cell.neighbors = []  # reset
                # check top
                if not cell.walls["top"] and r > 0:
                    cell.neighbors.append(self.grid[r - 1][c])
                # right
                if not cell.walls["right"] and c < self.cols - 1:
                    cell.neighbors.append(self.grid[r][c + 1])
                # bottom
                if not cell.walls["bottom"] and r < self.rows - 1:
                    cell.neighbors.append(self.grid[r + 1][c])
                # left
                if not cell.walls["left"] and c > 0:
                    cell.neighbors.append(self.grid[r][c - 1])
