import time
import tracemalloc


class PerformanceMetrics:
    def __init__(self):
        self.results = {}

    def measure(self, name, solver_function, *args):
        """
        قياس الزمن، عدد الخطوات، والذاكرة
        """
        tracemalloc.start()
        start_time = time.perf_counter()

        path = solver_function(*args)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.results[name] = {
            "time_ms": (end_time - start_time) * 1000,
            "steps": len(path),
            "memory_kb": peak / 1024
        }

        return path

    def print_results(self):
        """
        طباعة النتائج بشكل جدول
        """
        print("\nAlgorithm Performance Comparison")
        print("-" * 45)
        print(f"{'Algorithm':<12} | {'Time(ms)':<10} | {'Steps':<7} | {'Memory(KB)':<10}")
        print("-" * 45)

        for algo, data in self.results.items():
            print(
                f"{algo:<12} | "
                f"{data['time_ms']:<10.2f} | "
                f"{data['steps']:<7} | "
                f"{data['memory_kb']:<10.2f}"
            )
