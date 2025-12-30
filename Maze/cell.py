class Cell:
    def __init__(self, row, col):
        """
        تمثل هذه الفئة خلية واحدة في المتاهة
        """
        self.row = row
        self.col = col

        # الجدران الأربعة للخلية
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }

        # هل تمت زيارة الخلية (مهم للتوليد والحل)
        self.visited = False

        # لاستخدام خوارزميات المسار الأقصر
        self.distance = float("inf")  # Dijkstra
        self.parent = None            # لإعادة بناء المسار

    def remove_wall(self, other, wall):
        """
        إزالة الجدار بين هذه الخلية وخلية مجاورة
        """
        self.walls[wall] = False

        opposite_walls = {
            "top": "bottom",
            "bottom": "top",
            "left": "right",
            "right": "left"
        }
        other.walls[opposite_walls[wall]] = False

    def reset(self):
        """
        إعادة تعيين الخلية (قبل حل جديد)
        """
        self.visited = False
        self.distance = float("inf")
        self.parent = None
