import matplotlib.pyplot as plt


class MazeDrawer:
    def __init__(self, maze, cell_size=1):
        self.maze = maze
        self.cell_size = cell_size

    def draw_maze(self, path=None):
        """
        رسم المتاهة
        path: قائمة خلايا تمثل الحل (اختياري)
        """
        rows, cols = self.maze.rows, self.maze.cols

        plt.figure(figsize=(cols, rows))

        # رسم الجدران
        for row in self.maze.grid:
            for cell in row:
                x = cell.col * self.cell_size
                y = (rows - cell.row) * self.cell_size

                if cell.walls["top"]:
                    plt.plot([x, x + 1], [y, y], color="black")
                if cell.walls["right"]:
                    plt.plot([x + 1, x + 1], [y, y - 1], color="black")
                if cell.walls["bottom"]:
                    plt.plot([x, x + 1], [y - 1, y - 1], color="black")
                if cell.walls["left"]:
                    plt.plot([x, x], [y, y - 1], color="black")

        # رسم المسار إن وجد
        if path:
            xs = []
            ys = []
            for cell in path:
                xs.append(cell.col + 0.5)
                ys.append(rows - cell.row - 0.5)

            plt.plot(xs, ys, color="red", linewidth=2)

        plt.axis("off")
        plt.title("Maze Visualization")
        plt.show()
