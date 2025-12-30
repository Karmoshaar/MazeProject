from collections import deque


class MazeSolver:
    def __init__(self, maze):
        """
        يستقبل كائن Maze
        """
        self.maze = maze

    def solve_dfs(self, start, end):
        """
        حل المتاهة باستخدام DFS
        """
        stack = [start]
        start.visited = True

        while stack:
            current = stack.pop()

            if current == end:
                return self._reconstruct_path(end)

            for neighbor in self._get_valid_neighbors(current):
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.parent = current
                    stack.append(neighbor)

        return []

    def solve_bfs(self, start, end):
        """
        حل المتاهة باستخدام BFS (أقصر مسار)
        """
        queue = deque([start])
        start.visited = True

        while queue:
            current = queue.popleft()

            if current == end:
                return self._reconstruct_path(end)

            for neighbor in self._get_valid_neighbors(current):
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.parent = current
                    queue.append(neighbor)

        return []

    def _get_valid_neighbors(self, cell):
        """
        جيران بدون جدران بيننا وبينهم
        """
        neighbors = []
        r, c = cell.row, cell.col

        directions = [
            ("top", r - 1, c),
            ("right", r, c + 1),
            ("bottom", r + 1, c),
            ("left", r, c - 1)
        ]

        for wall, nr, nc in directions:
            if not cell.walls[wall]:
                neighbor = self.maze.get_cell(nr, nc)
                if neighbor:
                    neighbors.append(neighbor)

        return neighbors

    def _reconstruct_path(self, end_cell):
        """
        إعادة بناء المسار من النهاية للبداية
        """
        path = []
        current = end_cell

        while current:
            path.append(current)
            current = current.parent

        return path[::-1]
    def solve_dijkstra(self, start, end):
        """
        Dijkstra: أقصر مسار بدون heuristic
        """
        self._reset_distances()
        start.distance = 0

        pq = [(0, start)]

        while pq:
            dist, current = heapq.heappop(pq)

            if current.visited:
                continue

            current.visited = True

            if current == end:
                return self._reconstruct_path(end)

            for neighbor in self._get_valid_neighbors(current):
                new_dist = current.distance + 1
                if new_dist < neighbor.distance:
                    neighbor.distance = new_dist
                    neighbor.parent = current
                    heapq.heappush(pq, (neighbor.distance, neighbor))

        return []

    def solve_astar(self, start, end):
        """
        A*: Dijkstra + heuristic (Manhattan)
        """
        self._reset_distances()
        start.distance = 0

        pq = [(self._heuristic(start, end), start)]

        while pq:
            _, current = heapq.heappop(pq)

            if current.visited:
                continue

            current.visited = True

            if current == end:
                return self._reconstruct_path(end)

            for neighbor in self._get_valid_neighbors(current):
                tentative_g = current.distance + 1
                if tentative_g < neighbor.distance:
                    neighbor.distance = tentative_g
                    neighbor.parent = current
                    f = tentative_g + self._heuristic(neighbor, end)
                    heapq.heappush(pq, (f, neighbor))

        return []

    def _heuristic(self, a, b):
        """
        Manhattan Distance
        """
        return abs(a.row - b.row) + abs(a.col - b.col)

    def _reset_distances(self):
        for row in self.maze.grid:
            for cell in row:
                cell.visited = False
                cell.distance = float("inf")
                cell.parent = None