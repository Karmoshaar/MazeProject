import random


class MazeGenerator:
    def __init__(self, maze):
        """
        يستقبل كائن Maze
        """
        self.maze = maze

    def generate(self, start_row=0, start_col=0):
        """
        توليد المتاهة باستخدام Recursive Backtracking
        """
        start_cell = self.maze.get_cell(start_row, start_col)
        self._backtrack(start_cell)

    def _backtrack(self, current):
        """
        الخوارزمية الأساسية (DFS + Backtracking)
        """
        current.visited = True

        # جلب الجيران غير المزورين بترتيب عشوائي
        neighbors = self.maze.get_unvisited_neighbors(current)
        random.shuffle(neighbors)

        for neighbor in neighbors:
            if not neighbor.visited:
                self._remove_walls(current, neighbor)
                self._backtrack(neighbor)

    def _remove_walls(self, current, next_cell):
        """
        إزالة الجدار بين خليتين متجاورتين
        """
        dr = next_cell.row - current.row
        dc = next_cell.col - current.col

        if dr == -1:  # next فوق current
            current.remove_wall(next_cell, "top")
        elif dr == 1:  # next تحت current
            current.remove_wall(next_cell, "bottom")
        elif dc == -1:  # next يسار current
            current.remove_wall(next_cell, "left")
        elif dc == 1:  # next يمين current
            current.remove_wall(next_cell, "right")
