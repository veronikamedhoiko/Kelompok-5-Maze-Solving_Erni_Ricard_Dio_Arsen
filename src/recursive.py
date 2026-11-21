# ANGOTA_4:

"""Pencarian jalur Maze secara rekursif menggunakan DFS."""
def solve_recursive(maze):
    """Mengembalikan jalur pertama yang ditemukan atau None."""
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