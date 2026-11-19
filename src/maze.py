"""Representasi dan validasi labirin."""

class Maze:
    """Labirin berbasis tuple string; '#' adalah tembok dan '.' adalah jalan."""

    def __init__(self, rows):
        if not rows:
            raise ValueError("Maze tidak boleh kosong")
        width = len(rows[0])
        if width == 0 or any(len(row) != width for row in rows):
            raise ValueError("Semua baris Maze harus memiliki panjang sama")
        if any(set(row) - {".", "#", "S", "E"} for row in rows):
            raise ValueError("Karakter Maze hanya boleh '.', '#', 'S', atau 'E'")
        if sum(row.count("S") for row in rows) != 1:
            raise ValueError("Maze harus memiliki tepat satu titik awal S")
        if sum(row.count("E") for row in rows) != 1:
            raise ValueError("Maze harus memiliki tepat satu titik akhir E")
        self._rows = tuple(rows)
        self.height = len(rows)
        self.width = width
        self.start = self._find("S")
        self.end = self._find("E")

    def _find(self, marker):
        for row_index, row in enumerate(self._rows):
            column_index = row.find(marker)
            if column_index != -1:
                return (row_index, column_index)
        return None

    def is_open(self, position):
        """True jika posisi berada di dalam Maze dan bukan tembok."""
        row, column = position
        return (
            0 <= row < self.height
            and 0 <= column < self.width
            and self._rows[row][column] != "#"
        )

    def neighbors(self, position):
        """Mengembalikan tetangga valid: atas, kanan, bawah, kiri."""
        row, column = position
        candidates = (
            (row - 1, column),
            (row, column + 1),
            (row + 1, column),
            (row, column - 1),
        )
        return tuple(point for point in candidates if self.is_open(point))

    def render(self, path=()):
        """Menghasilkan tampilan teks Maze dengan jalur bertanda '*'."""
        path_set = set(path)
        output = []
        for row_index, row in enumerate(self._rows):
            line = []
            for column_index, cell in enumerate(row):
                point = (row_index, column_index)
                if point in path_set and cell not in ("S", "E"):
                    line.append("*")
                else:
                    line.append(cell)
            output.append("".join(line))
        return "\n".join(output)
