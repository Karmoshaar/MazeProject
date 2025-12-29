import random

class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        # مصفوفة لتتبع الخلايا المزارة
        self.visited = [[False for _ in range(cols)] for _ in range(rows)]

        # كل خلية لها أربعة جدران
        self.maze = [[{
            'top': True,
            'right': True,
            'bottom': True,
            'left': True
        } for _ in range(cols)] for _ in range(rows)]

    def generate(self, r=0, c=0):
        """توليد المتاهة باستخدام DFS"""
        self.visited[r][c] = True

        directions = ['top', 'right', 'bottom', 'left']
        random.shuffle(directions)

        for direction in directions:
            nr, nc = r, c

            if direction == 'top':
                nr -= 1
            elif direction == 'right':
                nc += 1
            elif direction == 'bottom':
                nr += 1
            elif direction == 'left':
                nc -= 1

            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if not self.visited[nr][nc]:
                    self.remove_wall(r, c, nr, nc, direction)
                    self.generate(nr, nc)

    def remove_wall(self, r, c, nr, nc, direction):
        """إزالة الجدار بين خليتين"""
        if direction == 'top':
            self.maze[r][c]['top'] = False
            self.maze[nr][nc]['bottom'] = False
        elif direction == 'right':
            self.maze[r][c]['right'] = False
            self.maze[nr][nc]['left'] = False
        elif direction == 'bottom':
            self.maze[r][c]['bottom'] = False
            self.maze[nr][nc]['top'] = False
        elif direction == 'left':
            self.maze[r][c]['left'] = False
            self.maze[nr][nc]['right'] = False
