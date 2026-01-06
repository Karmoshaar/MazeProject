class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
