from maze.maze import Maze
from maze.generator import MazeGenerator
from maze.solver import MazeSolver
from visualization.draw import MazeDrawer

def main():
    rows, cols = 15, 15
    maze = Maze(rows, cols)

    MazeGenerator(maze).generate(0, 0)

    start = maze.grid[1][1]
    end = maze.grid[rows-2][cols-2]

    solver = MazeSolver(maze)
    path = solver.solve_a_star(start, end)

    MazeDrawer().draw(maze, path)

if __name__ == "__main__":
    main()
