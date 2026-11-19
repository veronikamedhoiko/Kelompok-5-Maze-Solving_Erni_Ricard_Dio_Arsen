"""Pencarian jalur Maze secara rekursif menggunakan Depth-First Search."""


def solve_recursive(maze):
    """Mencari jalur dari S ke E secara rekursif.

    Mengembalikan tuple koordinat dari S ke E, atau None jika tidak ada jalur.
    """
    visited = set()
    path = []

    def visit(position):
        if position == maze.end:
            path.append(position)
            return True
        if position in visited:
            return False

        visited.add(position)
        path.append(position)

        for neighbor in maze.neighbors(position):
            if neighbor not in visited and visit(neighbor):
                return True

        path.pop()
        return False

    if visit(maze.start):
        return tuple(path)
    return None
