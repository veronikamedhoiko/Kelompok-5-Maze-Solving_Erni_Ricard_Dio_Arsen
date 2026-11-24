# ANGGOTA_01:

# Membuat Gragik Untuk Waktu Dan Memory
import matplotlib.pyplot as plt

# Pengujian Waktu Dan Memori

import gc
import statistics
import time
import tracemalloc
import matplotlib.pyplot as plt

from src.maze import Maze
from src.iterative import solve_bfs
from src.recursive import solve_recursive


# Data Maze
ROWS = (
    "S.........",
    ".####.....",
    ".....#....",
    ".....#....",
    ".....#....",
    "..........",
    "....###...",
    "..........",
    ".........#",
    ".........E",
)

RUNS = 1000
REPEATS = 7

# 1. Fungsi pengukuran waktu
def measure_time(function, maze):
    results = []

    for _ in range(REPEATS):
        start_time = time.perf_counter()
        for _ in range(RUNS):
            function(maze)
        end_time = time.perf_counter()
        results.append((end_time - start_time) / RUNS)
    return statistics.median(results)

# 2. Fungsi pengukuran memori
def measure_memory(function, maze):
    gc.collect()
    tracemalloc.start()
    try:
        before_memory, _ = tracemalloc.get_traced_memory()
        tracemalloc.reset_peak()
        function(maze)
        _, peak_memory = tracemalloc.get_traced_memory()
        memory_used = max(0, peak_memory - before_memory)
        return memory_used / 1024
    finally:
        tracemalloc.stop()

# 3. Program utama benchmark
def show_graph(time_results, memory_results):
    """Menampilkan grafik waktu dan penggunaan memori."""

    names = list(time_results.keys())

    # Grafik waktu
    time_values = [
        time_results[name] * 1000
        for name in names
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(names, time_values)

    plt.title("Perbandingan Waktu Eksekusi BFS dan DFS")
    plt.xlabel("Algoritma")
    plt.ylabel("Waktu (milidetik)")

    for index, value in enumerate(time_values):
        plt.text(
            index,
            value,
            f"{value:.4f} ms",
            ha="center"
        )

    plt.tight_layout()
    plt.savefig("grafik_waktu.png")
    plt.show()

    # Grafik memori
    memory_values = [
        memory_results[name]
        for name in names
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(names, memory_values)

    plt.title("Perbandingan Penggunaan Memori BFS dan DFS")
    plt.xlabel("Algoritma")
    plt.ylabel("Memori (KB)")

    for index, value in enumerate(memory_values):
        plt.text(
            index,
            value,
            f"{value:.2f} KB",
            ha="center"
        )

    plt.tight_layout()
    plt.savefig("grafik_memori.png")
    plt.show()

def show_maze_images(rows, bfs_path, dfs_path):
    """Menampilkan tiga gambar hasil Maze Solving."""

    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    def draw_maze(path, title, path_color, filename):
        height = len(rows)
        width = len(rows[0])
        path_set = set(path or ())

        maze_data = []

        for r in range(height):
            line = []

            for c in range(width):
                cell = rows[r][c]

                if cell == "#":
                    line.append(1)
                elif (r, c) in path_set:
                    line.append(2)
                else:
                    line.append(0)

            maze_data.append(line)

        colors = ["white", "#4B5563", path_color]
        cmap = ListedColormap(colors)

        fig, ax = plt.subplots(figsize=(8, 7))

        ax.imshow(maze_data, cmap=cmap, vmin=0, vmax=2)
        ax.set_xticks(range(width + 1), minor=True)
        ax.set_yticks(range(height + 1), minor=True)
        ax.grid(which="minor", color="black", linewidth=1.2)
        ax.tick_params(
            which="both",
            bottom=False,
            left=False,
            labelbottom=False,
            labelleft=False
        )

        for r in range(height):
            for c in range(width):
                if rows[r][c] == "S":
                    ax.text(
                        c, r, "S",
                        ha="center", va="center",
                        fontsize=16, color="green",
                        fontweight="bold"
                    )
                elif rows[r][c] == "E":
                    ax.text(
                        c, r, "E",
                        ha="center", va="center",
                        fontsize=16, color="red",
                        fontweight="bold"
                    )

        steps = len(path) - 1 if path else 0

        ax.set_title(
            f"{title}\nJumlah langkah: {steps}"
        )

        plt.tight_layout()
        plt.savefig(filename, dpi=150)

    draw_maze(None, "MAZE AWAL", "white", "maze_awal.png")
    draw_maze(bfs_path, "BFS (ITERATIVE)", "#2685E8", "maze_bfs.png")
    draw_maze(dfs_path, "DFS (RECURSIVE)", "#FF991F", "maze_dfs.png")

    plt.show()

def main():
    """Menjalankan benchmark dan menampilkan grafik."""

    maze = Maze(ROWS)

 # Menghitung jalur BFS dan DFS
    bfs_path = solve_bfs(maze)
    dfs_path = solve_recursive(maze)

    # Menampilkan tiga gambar Maze
    show_maze_images(ROWS, bfs_path, dfs_path)

    algorithms = {
        "BFS (Iterative)": solve_bfs,
        "DFS (Recursive)": solve_recursive,
    }

    print("=" * 55)
    print("BENCHMARK MAZE SOLVING")
    print("=" * 55)

    # Menampilkan maze awal
    print("\nMAZE AWAL")
    print(maze.render())

    # Menampilkan hasil jalur
    for name, function in algorithms.items():
        print(f"\nHASIL {name}")

        path = function(maze)

        if path is None:
            print("Jalur tidak ditemukan!")
        else:
            print("Jalur ditemukan!")
            print("Jumlah langkah:", len(path) - 1)
            print(maze.render(path))

    # Menyimpan hasil waktu dan memori
    time_results = {}
    memory_results = {}

    print("\nHASIL PENGUKURAN WAKTU")
    print("-" * 55)

    for name, function in algorithms.items():
        elapsed = measure_time(function, maze)
        time_results[name] = elapsed

        print(f"{name}: {elapsed:.8f} detik")

    print("\nHASIL PENGUKURAN MEMORI")
    print("-" * 55)

    for name, function in algorithms.items():
        memory_samples = []

        for _ in range(REPEATS):
            memory = measure_memory(function, maze)
            memory_samples.append(memory)

        memory = statistics.median(memory_samples)
        memory_results[name] = memory
        print(f"{name}: {memory:.4f} KB")

    # Membuat grafik
    print("\nMembuat grafik perbandingan...")
    show_graph(time_results, memory_results)

    print("\nBENCHMARK SELESAI")

if __name__ == "__main__":
    main()