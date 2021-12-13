test_data = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]

class OctoGrid:
    def __init__(self, lines):
        self.width = len(lines[0].strip())
        self.height = len(lines)
        self.grid = []
        for line in lines:
            for c in line.strip():
                self.grid.append(int(c))

    def __str__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += str(self.grid[self._to_index(x, y)])
            s += '\n'
        return s

    def _to_index(self, x, y):
        return y * self.width + x

    def _from_index(self, index):
        return index % self.width, index // self.width

    def _spread_flash(self, index, flashed):
        x, y = self._from_index(index)

        adjacents = [
            (-1,-1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]

        for adj in adjacents:
            nx, ny = x + adj[0], y + adj[1]

            if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height:
                adj_index = self._to_index(nx, ny)
                if adj_index not in flashed:
                    self.grid[adj_index] += 1
    

    def _process_flashes(self, flashed):
        flash_count = 0
        for y in range(self.height):
            for x in range(self.width):
                i = self._to_index(x, y)
                if self.grid[i] > 9 and i not in flashed:
                    self.grid[i] = 0
                    flash_count += 1
                    self._spread_flash(i, flashed)
                    flashed.add(i)

        return flash_count


    def step(self):
        flash_count = 0
        self.grid = [x + 1 for x in self.grid]

        flashed = set()
        fc = self._process_flashes(flashed)
        while fc > 0:
            flash_count += fc
            fc = self._process_flashes(flashed)
        return flash_count

def main():
    with open('input.txt') as input_file:
        og = OctoGrid(input_file.readlines())

        flash_count = 0
        step = 1
        had_sync = False
        while True:
            step_flash_count = og.step()
           
            if step_flash_count == og.width * og.height:
                print(f"Synchronised flash happened at step {step}")
                had_sync = True

            flash_count += step_flash_count

            if step == 100:
                print(f"Flash count at step 100: {flash_count}")

            if step >= 99 and had_sync:
                break

            step += 1

main()