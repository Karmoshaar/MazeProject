from maze.cell import Cell


class Maze:
    def __init__(self, rows, cols):
        """
        تمثل هذه الفئة المتاهة كاملة (Grid of Cells)
        """
        self.rows = rows
        self.cols = cols

        # إنشاء الشبكة
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    def get_cell(self, row, col):
        """
        إرجاع خلية حسب الإحداثيات
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def get_neighbors(self, cell):
        """
        إرجاع جميع الجيران (بدون اعتبار الجدران)
        """
        neighbors = []
        r, c = cell.row, cell.col

        top = self.get_cell(r - 1, c)
        right = self.get_cell(r, c + 1)
        bottom = self.get_cell(r + 1, c)
        left = self.get_cell(r, c - 1)

        if top:
            neighbors.append(top)
        if right:
            neighbors.append(right)
        if bottom:
            neighbors.append(bottom)
        if left:
            neighbors.append(left)

        return neighbors

    def get_unvisited_neighbors(self, cell):
        """
        جيران لم تتم زيارتهم (مهم لتوليد المتاهة)
        """
        return [n for n in self.get_neighbors(cell) if not n.visited]

    def reset_cells(self):
        """
        إعادة تعيين جميع الخلايا (قبل حل جديد)
        """
        for row in self.grid:
            for cell in row:
                cell.reset()
