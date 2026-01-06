from maze.maze import Maze
from maze.generator import MazeGenerator
from maze.solver import MazeSolver
from visualization.draw import MazeDrawer
from analysis.metrics import Metrics 

def main():
    print("MAIN STARTED ✅")

    # إنشاء المتاهة
    maze = Maze(10, 10)
    generator = MazeGenerator(maze)
    generator.generate()
    maze.link_neighbors()
    print("Maze generated.")


    # الأدوات
    solver = MazeSolver(maze)
    metrics = Metrics()
    drawer = MazeDrawer()

    # البداية والنهاية
    start = maze.grid[0][0]
    end = maze.grid[maze.rows - 1][maze.cols - 1]

    # تشغيل الخوارزميات + القياس
    results = []
    results.append(metrics.measure("DFS", solver.solve_dfs, start, end))
    results.append(metrics.measure("BFS", solver.solve_bfs, start, end))
    results.append(metrics.measure("Dijkstra", solver.solve_dijkstra, start, end))
    results.append(metrics.measure("A*", solver.solve_a_star, start, end))

    # 🔹 الطباعة (قبل الرسم)
    print("\nAlgorithm Performance Comparison")
    print("---------------------------------------------")
    metrics.print_results(results)

    # 🔹 الرسم (آخر شيء)
    best_path = solver.solve_a_star(start, end)
    drawer.draw(maze, best_path)


if __name__ == "__main__":
    main()
