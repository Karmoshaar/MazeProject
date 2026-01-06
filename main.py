from maze.maze import Maze
from maze.generator import MazeGenerator
from maze.solver import MazeSolver
from visualization.draw import MazeDrawer
from analysis.metrics import PerformanceMetrics


def main():
    # إعداد حجم المتاهة
    ROWS = 15
    COLS = 15

    # إنشاء المتاهة
    maze = Maze(ROWS, COLS)

    # توليد المتاهة
    generator = MazeGenerator(maze)
    generator.generate(0, 0)

    # نقاط البداية والنهاية
    start = maze.get_cell(0, 0)
    end = maze.get_cell(ROWS - 1, COLS - 1)

    # كائن الحل
    solver = MazeSolver(maze)

    # كائن القياس
    metrics = PerformanceMetrics()

    # تشغيل الخوارزميات + القياس
    path_dfs = metrics.measure("DFS", solver.solve_dfs, start, end)
    maze.reset_cells()

    path_bfs = metrics.measure("BFS", solver.solve_bfs, start, end)
    maze.reset_cells()

    path_dijkstra = metrics.measure("Dijkstra", solver.solve_dijkstra, start, end)
    maze.reset_cells()

    path_astar = metrics.measure("A*", solver.solve_a_star, start, end)

    # طباعة نتائج المقارنة
    metrics.print_results()

    # العرض المرئي (اختَر أي مسار)
    drawer = MazeDrawer(maze)
    drawer.draw_maze(path_astar)


if __name__ == "__main__":
    main()
