import heapq
import itertools
from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    # ===================== BFS =====================
    def solve_bfs(self, start, end):
        queue = deque([start])
        visited = {start}
        parent = {}

        while queue:
            current = queue.popleft()
            if current == end:
                return self._reconstruct_path(parent, start, end)

            for neighbor in self.maze.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        return []

    # ===================== DFS =====================
    def solve_dfs(self, start, end):
        stack = [start]
        visited = {start}
        parent = {}

        while stack:
            current = stack.pop()
            if current == end:
                return self._reconstruct_path(parent, start, end)

            for neighbor in self.maze.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append(neighbor)

        return []

    # ===================== Dijkstra =====================
    def solve_dijkstra(self, start, end):
        counter = itertools.count()
        pq = []
        heapq.heappush(pq, (0, next(counter), start))

        distances = {start: 0}
        parent = {}

        while pq:
            dist, _, current = heapq.heappop(pq)

            if current == end:
                return self._reconstruct_path(parent, start, end)

            for neighbor in self.maze.get_neighbors(current):
                new_dist = dist + 1
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = current
                    heapq.heappush(
                        pq,
                        (new_dist, next(counter), neighbor)
                    )

        return []

    # ===================== A* =====================
    def solve_a_star(self, start, end):
        counter = itertools.count()
        pq = []
        heapq.heappush(pq, (0, next(counter), start))

        g_score = {start: 0}
        parent = {}

        while pq:
            _, _, current = heapq.heappop(pq)

            if current == end:
                return self._reconstruct_path(parent, start, end)

            for neighbor in self.maze.get_neighbors(current):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self._heuristic(neighbor, end)
                    parent[neighbor] = current
                    heapq.heappush(
                        pq,
                        (f_score, next(counter), neighbor)
                    )

        return []

    # ===================== Helpers =====================
    def _heuristic(self, a, b):
        return abs(a.row - b.row) + abs(a.col - b.col)

    def _reconstruct_path(self, parent, start, end):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = parent.get(current)
            if current is None:
                return []
        path.append(start)
        path.reverse()
        return path
