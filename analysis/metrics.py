class Metrics :
    def __init__(self):
        pass

    def measure(self, name, func, *args):
        import time
        import tracemalloc

        tracemalloc.start()
        start_time = time.perf_counter()

        path = func(*args)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return {
            "name": name,
            "time": (end_time - start_time) * 1000,
            "steps": len(path),
            "memory": peak / 1024
        }

    def print_results(self, results):
        print("\nAlgorithm Performance Comparison")
        print("-" * 45)
        print(f"{'Algorithm':<12} | {'Time(ms)':<9} | {'Steps':<7} | {'Memory(KB)'}")
        print("-" * 45)

        for r in results:
            print(f"{r['name']:<12} | {r['time']:<9.2f} | {r['steps']:<7} | {r['memory']:.2f}")
