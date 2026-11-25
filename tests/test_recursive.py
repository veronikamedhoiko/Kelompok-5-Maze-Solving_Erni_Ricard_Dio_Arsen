
# ANGGOTA_4:
# Pengujian Algoritma Recursive DFS

import unittest
from src.recursive import solve_recursive


class MazeStub:
    """Representasi maze sederhana untuk pengujian recursive."""

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def neighbors(self, position):
        return self.graph.get(position, [])


class TestRecursive(unittest.TestCase):

    def test_path_found(self):
        """Menguji ketika jalur menuju tujuan ditemukan."""

        maze = MazeStub(
            {
                "S": ["A"],
                "A": ["E"],
                "E": []
            },
            "S",
            "E"
        )

        result = solve_recursive(maze)

        self.assertEqual(result, ("S", "A", "E"))

    def test_no_path_found(self):
        """Menguji ketika jalur menuju tujuan tidak tersedia."""

        maze = MazeStub(
            {
                "S": ["A"],
                "A": ["S"],
                "E": []
            },
            "S",
            "E"
        )

        result = solve_recursive(maze)

        self.assertIsNone(result)

    def test_backtracking(self):
        """Menguji proses kembali ketika menemukan jalan buntu."""

        maze = MazeStub(
            {
                "S": ["A", "B"],
                "A": ["C"],
                "C": [],
                "B": ["E"],
                "E": []
            },
            "S",
            "E"
        )

        result = solve_recursive(maze)

        self.assertEqual(result, ("S", "B", "E"))
        self.assertNotIn("A", result)
        self.assertNotIn("C", result)

    def test_cycle_detection(self):
        """Menguji agar pencarian tidak terjebak dalam siklus."""

        maze = MazeStub(
            {
                "S": ["A"],
                "A": ["B"],
                "B": ["S", "C"],
                "C": ["A"]
            },
            "S",
            "E"
        )

        result = solve_recursive(maze)

        self.assertIsNone(result)

    def test_start_is_goal(self):
        """Menguji ketika titik awal sama dengan tujuan."""

        maze = MazeStub(
            {
                "S": []
            },
            "S",
            "S"
        )

        result = solve_recursive(maze)

        self.assertEqual(result, ("S",))


if __name__ == "__main__":
    unittest.main()
