# ANGOTA_4:

"""Pencarian jalur Maze secara iteratif menggunakan BFS dan Queue."""
from src.queue import Queue
 
def solve_bfs(maze):
    """Mengembalikan jalur terpendek S ke E, atau None jika tidak ada."""
    frontier = Queue()
    frontier.enqueue(maze.start)
    parents = {maze.start: None}
    while not frontier.is_empty():
        current = frontier.dequeue()
        if current == maze.end:
            return _build_path(parents, current)
        for neighbor in maze.neighbors(current):
            if neighbor not in parents:
                parents[neighbor] = current
                frontier.enqueue(neighbor)
    return None
def _build_path(parents, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return tuple(path)