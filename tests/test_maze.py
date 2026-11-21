import unittest
from src.maze import Maze

class TestMaze(unittest.TestCase):
    def test_valid_maze(self):
        maze = Maze(("S.E",))
        self.assertEqual(maze.start, (0, 0))
        self.assertEqual(maze.end, (0, 2))
        self.assertTrue(maze.is_open((0, 1)))
    def test_invalid_empty_or_ragged_maze(self):
        with self.assertRaises(ValueError):
            Maze(())
        with self.assertRaises(ValueError):
            Maze(("S.", "E"))
    def test_invalid_markers_and_characters(self):
        with self.assertRaises(ValueError):
            Maze(("...",))
        with self.assertRaises(ValueError):
            Maze(("S.E", "S.."))
        with self.assertRaises(ValueError):
            Maze(("S?E",))
    def test_neighbors_and_render(self):
        maze = Maze(("S.", ".E"))
        self.assertEqual(set(maze.neighbors((0, 0))), {(0, 1), (1, 0)})
        self.assertIn("*", maze.render(((0, 0), (0, 1), (1, 1))))

if __name__ == "__main__":
    unittest.main()
