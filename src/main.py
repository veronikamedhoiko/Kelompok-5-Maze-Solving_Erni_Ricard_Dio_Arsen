# ANGGOTA_01:

"""Program utama demonstrasi Maze Solving."""
from src.maze import Maze
from src.iterative import solve_bfs
from src.recursive import solve_recursive

def main():
    rows = (
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
    maze = Maze(rows)
    bfs_path = solve_bfs(maze)
    dfs_path = solve_recursive(maze)
    
    print("=== MAZE SOLVING ===")
    print("\nMaze awal:")
    print(maze.render())

    print("\nHasil BFS (iteratif):")
    print("Jalur:", bfs_path)
    print("Jumlah langkah:", len(bfs_path) - 1 if bfs_path else "Tidak ditemukan")
    print(maze.render(bfs_path or ()))

    print("\nHasil DFS (rekursif):")
    print("Jalur:", dfs_path)
    print("Jumlah langkah:", len(dfs_path) - 1 if dfs_path else "Tidak ditemukan")
    print(maze.render(dfs_path or ()))
if __name__ == "__main__":
    main()