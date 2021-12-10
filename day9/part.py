
class HeightMap:
    def __init__(self, lines):
        self.grid = []
        self.height = len(lines)
        self.width = len(lines[0].strip())

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
    
    def _lower(self, x0, y0, x1, y1):
        i0 = self._to_index(x0, y0)
        i1 = self._to_index(x1, y1)
        return self.grid[i0] < self.grid[i1]

    def _check_location(self, x, y):
        if x > 0:
            if not self._lower(x, y, x - 1, y):
                return False
        if x < self.width-1:
            if not self._lower(x, y, x + 1, y):
                return False
        
        if y > 0:
            if not self._lower(x, y, x, y - 1):
                return False
        if y < self.height-1:
            if not self._lower(x, y, x, y + 1):
                return False
        return True

    def _is_valid_point(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height


    def get_value(self, index):
        return self.grid[index]

    def get_lowpoints(self):
        points = []
        for y in range(self.height):
            for x in range(self.width):
                if self._check_location(x,y):
                    points.append(self._to_index(x, y))
        return points

    def get_lowpoint_basin(self, lowpoint):
        queue = [lowpoint]
        basin = set([lowpoint])
        
        while len(queue) > 0:
            pt = queue.pop(0)
            value = self.get_value(pt)
            x,y = self._from_index(pt)

            adjacent = [
                (x-1, y),
                (x+1, y),
                (x, y+1),
                (x, y-1)
            ]

            for adj in adjacent:
                x1, y1 = adj
                if self._is_valid_point(x1, y1):
                    adj_pt = self._to_index(x1, y1)
                    adj_val = self.get_value(adj_pt)
                    if adj_val < 9 and value < adj_val:
                        basin.add(adj_pt)
                        queue.append(adj_pt)
        return list(basin)


def test_part1():
    test_data = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]

    hm = HeightMap(test_data)
    points = hm.get_lowpoints()
    print(points)
    print([hm.get_value(p) for p in points])
    print(sum([1 + hm.get_value(x) for x in points]))


def part1():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        hm = HeightMap(lines)
        points = hm.get_lowpoints()
        print(sum([1 + hm.get_value(x) for x in points]))

test_part1()
#part1()

def test_part2():
    test_data = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]

    hm = HeightMap(test_data)
    points = hm.get_lowpoints()
    basins = []
    for point in points:
        basins.append(hm.get_lowpoint_basin(point))

    sizes = [len(b) for b in basins]
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

def part2():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        hm = HeightMap(lines)
        points = hm.get_lowpoints()
        basins = []
        for point in points:
            basins.append(hm.get_lowpoint_basin(point))

        sizes = [len(b) for b in basins]
        sizes.sort(reverse=True)
        print(sizes[0] * sizes[1] * sizes[2])

    
#test_part2()
part2()


