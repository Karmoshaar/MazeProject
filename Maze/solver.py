import heapq
from itertools import count
from typing import Dict, List, Optional
from .cell import Cell
from .maze import Maze

INF = float("inf")

class MazeSolver:
    def __init__(self, maze: Maze):
        self.maze = maze

    def _reconstruct_path(
        self,
        came_from: Dict[Cell, Optional[Cell]],
        start: Cell,
        end: Cell
    ) -> List[Cell]:
        if end not in came_from and end != start:
            return []

        path = []
        current = end
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

    # ---------------- DFS ----------------
    def solve_dfs(self, start: Cell, end: Cell) -> List[Cell]:
        stack = [start]
        came_from = {}
        visited = {start}

        while stack:
            current = stack.pop()
            if current == end:
                break

            for n in current.neighbors:
                if n not in visited:
                    visited.add(n)
                    came_from[n] = current
                    stack.append(n)

        return self._reconstruct_path(came_from, start, end)

    # ---------------- BFS ----------------
    def solve_bfs(self, start: Cell, end: Cell) -> List[Cell]:
        from collections import deque
        queue = deque([start])
        came_from = {}
        visited = {start}

        while queue:
            current = queue.popleft()
            if current == end:
                break

            for n in current.neighbors:
                if n not in visited:
                    visited.add(n)
                    came_from[n] = current
                    queue.append(n)

        return self._reconstruct_path(came_from, start, end)

    # ---------------- Dijkstra ----------------
    def solve_dijkstra(self, start: Cell, end: Cell) -> List[Cell]:
        pq = []
        counter = count()
        heapq.heappush(pq, (0, next(counter), start))

        dist = {start: 0}
        came_from = {}

        while pq:
            cost, _, current = heapq.heappop(pq)

            if current == end:
                break

            for n in current.neighbors:
                new_cost = cost + 1
                if new_cost < dist.get(n, INF):
                    dist[n] = new_cost
                    came_from[n] = current
                    heapq.heappush(pq, (new_cost, next(counter), n))

        return self._reconstruct_path(came_from, start, end)

    # ---------------- A* ----------------
    def solve_a_star(self, start: Cell, end: Cell) -> List[Cell]:
        def heuristic(a: Cell, b: Cell):
            return abs(a.row - b.row) + abs(a.col - b.col)

        pq = []
        counter = count()
        heapq.heappush(pq, (0, next(counter), start))

        came_from = {}
        g_score = {start: 0}

        while pq:
            _, _, current = heapq.heappop(pq)

            if current == end:
                break

            for n in current.neighbors:
                tentative = g_score[current] + 1
                if tentative < g_score.get(n, INF):
                    came_from[n] = current
                    g_score[n] = tentative
                    f = tentative + heuristic(n, end)
                    heapq.heappush(pq, (f, next(counter), n))

        return self._reconstruct_path(came_from, start, end)
