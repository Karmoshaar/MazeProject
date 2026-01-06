import heapq
import itertools
from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve_bfs(self, start, end):
        queue = deque([start])
        visited = {start}
        parent = {}

        while queue:
            current = queue.popleft()
            if current == end:
                return self._path(parent, start, end)

            for n in self.maze.get_neighbors(current):
                if n not in visited:
                    visited.add(n)
                    parent[n] = current
                    queue.append(n)
        return []

    def solve_dfs(self, start, end):
        stack = [start]
        visited = {start}
        parent = {}

        while stack:
            current = stack.pop()
            if current == end:
                return self._path(parent, start, end)

            for n in self.maze.get_neighbors(current):
                if n not in visited:
                    visited.add(n)
                    parent[n] = current
                    stack.append(n)
        return []

    def solve_dijkstra(self, start, end):
        counter = itertools.count()
        pq = [(0, next(counter), start)]
        dist = {start: 0}
        parent = {}

        while pq:
            d, _, current = heapq.heappop(pq)
            if current == end:
                return self._path(parent, start, end)

            for n in self.maze.get_neighbors(current):
                nd = d + 1
                if n not in dist or nd < dist[n]:
                    dist[n] = nd
                    parent[n] = current
                    heapq.heappush(pq, (nd, next(counter), n))
        return []

    def solve_a_star(self, start, end):
        counter = itertools.count()
        pq = [(0, next(counter), start)]
        g = {start: 0}
        parent = {}

        while pq:
            _, _, current = heapq.heappop(pq)
            if current == end:
                return self._path(parent, start, end)

            for n in self.maze.get_neighbors(current):
                temp = g[current] + 1
                if n not in g or temp < g[n]:
                    g[n] = temp
                    f = temp + abs(n.row - end.row) + abs(n.col - end.col)
                    parent[n] = current
                    heapq.heappush(pq, (f, next(counter), n))
        return []

    def _path(self, parent, start, end):
        path = []
        cur = end
        while cur != start:
            path.append(cur)
            cur = parent.get(cur)
            if cur is None:
                return []
        path.append(start)
        return path[::-1]
