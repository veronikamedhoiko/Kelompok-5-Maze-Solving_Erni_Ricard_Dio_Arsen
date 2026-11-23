# ANGGOTA_4:

import unittest
from src.maze import Maze
from src.iterative import solve_bfs

class TestIterative(unittest.TestCase):
    def test_bfs_finds_shortest_path(self):
        maze = Maze(("S.E",))
        self.assertEqual(solve_bfs(maze), ((0, 0), (0, 1), (0, 2)))
    def test_bfs_no_path(self):
        self.assertIsNone(solve_bfs(Maze(("S#E",))))
    def test_bfs_path_starts_and_ends_correctly(self):
        maze = Maze(("S..", "##.", "..E"))
        path = solve_bfs(maze)
        self.assertEqual(path[0], maze.start)
        self.assertEqual(path[-1], maze.end)

if __name__ == "__main__":
    unittest.main()