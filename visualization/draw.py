import matplotlib.pyplot as plt

class MazeDrawer:
    def draw(self, maze, path=None):
        fig, ax = plt.subplots()

        for row in maze.grid:
            for cell in row:
                x, y = cell.col, cell.row
                if cell.walls["top"]:
                    ax.plot([x, x+1], [y, y], color="black")
                if cell.walls["right"]:
                    ax.plot([x+1, x+1], [y, y+1], color="black")
                if cell.walls["bottom"]:
                    ax.plot([x, x+1], [y+1, y+1], color="black")
                if cell.walls["left"]:
                    ax.plot([x, x], [y, y+1], color="black")

        if path:
            xs = [c.col + 0.5 for c in path]
            ys = [c.row + 0.5 for c in path]
            ax.plot(xs, ys, color="red", linewidth=2)

        ax.set_aspect("equal")
        ax.invert_yaxis()
        plt.show()
