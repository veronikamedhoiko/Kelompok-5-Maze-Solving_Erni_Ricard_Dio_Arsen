import unittest

from src.maze import Maze
from src.recursive import solve_recursive


class TestRecursive(unittest.TestCase):

    def test_recursive_finds_path(self):
        maze = Maze(("S.E",))
        path = solve_recursive(maze)
        self.assertEqual(path[0], maze.start)
        self.assertEqual(path[-1], maze.end)

    def test_recursive_no_path(self):
        maze = Maze(("S#E",))
        self.assertIsNone(solve_recursive(maze))

    def test_recursive_avoids_walls(self):
        maze = Maze(("S#.", ".#.", "..E"))
        path = solve_recursive(maze)
        self.assertIsNotNone(path)
        for point in path:
            self.assertTrue(maze.is_open(point))


if __name__ == "__main__":
    unittest.main()
