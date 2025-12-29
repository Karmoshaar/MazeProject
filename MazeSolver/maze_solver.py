from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    def solve(self, start=(0, 0), end=None):
        if end is None:
            end = (self.rows - 1, self.cols - 1)

        queue = deque([start])
        visited = set([start])
        parent = {}

        while queue:
            r, c = queue.popleft()

            if (r, c) == end:
                return self.build_path(parent, start, end)

            for nr, nc in self.get_neighbors(r, c):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

        return None  # لا يوجد مسار

    def get_neighbors(self, r, c):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < self.rows and
                0 <= nc < self.cols and
                self.maze[nr][nc] == 0
            ):
                neighbors.append((nr, nc))

        return neighbors

    def build_path(self, parent, start, end):
        path = []
        current = end

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()
        return path


if __name__ == "__main__":
    maze = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    solver = MazeSolver(maze)
    path = solver.solve()

    print("Path:", path)
