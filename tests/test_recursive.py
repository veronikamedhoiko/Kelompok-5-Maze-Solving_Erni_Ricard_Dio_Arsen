# ANGOTA_4:

import unittest 
from src.recursive import solve_recursive

class MazeStub:
    """Maze sederhana untuk pengujian Recursive."""

    def __init__(self, start, end, graph):
        self.start = start
        self.end = end
        self.graph = graph

    def neighbors(self, position):
        return self.graph.get(position, [])

class TestRecursive(unittest.TestCase):

    def test_recursive(self):
         """Pengujian algoritma DFS Recursive."""
    def test_recursive_finds_path(self):
        maze = MazeStub(
            start=(0, 0),
            end=(0, 2),
            graph={
                (0, 0): [(0, 1)],
                (0, 1): [(0, 2)],
                (0, 2): []
            }
        )

        result = solve_recursive(maze)

        self.assertEqual(
            result,
            ((0, 0), (0, 1), (0, 2))
        )

    def test_recursive_no_path(self):
        maze = MazeStub(
            start=(0, 0),
            end=(2, 2),
            graph={
                (0, 0): [(0, 1)],
                (0, 1): []
            }
        )

        result = solve_recursive(maze)

        self.assertIsNone(result)

    def test_recursive_start_equals_end(self):
        maze = MazeStub(
            start=(0, 0),
            end=(0, 0),
            graph={}
        )

        result = solve_recursive(maze)

        self.assertEqual(result, ((0, 0),))

    def test_recursive_with_cycle(self):
        maze = MazeStub(
            start=(0, 0),
            end=(0, 2),
            graph={
                (0, 0): [(0, 1)],
                (0, 1): [(0, 0), (0, 2)],
                (0, 2): []
            }
        )

        result = solve_recursive(maze)

        self.assertEqual(
            result,
            ((0, 0), (0, 1), (0, 2))
        )
    if __name__ == "__main__":
        unittest.main()