"""
Cell representation for MazeProject.
Each cell knows its position and which walls exist.
"""
from typing import Dict, List

class Cell:
    __slots__ = ("row", "col", "walls", "neighbors")

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

        # walls: True means wall exists
        self.walls: Dict[str, bool] = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True,
        }

        # neighbors will be populated by Maze.link_neighbors()
        self.neighbors: List["Cell"] = []

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        return (self.row, self.col) == (other.row, other.col)

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"
