import sys

class Map:
    def __init__(self, lines):
        self.grid = []
        self.width = len(lines[0].strip())
        self.height = len(lines)
        for line in lines:
            for c in line.rstrip():
                self.grid.append(int(c))
    
    def _to_index(self, x, y):
        return y * self.width + x

    def _from_index(self, index):
        return index % self.width, index // self.width

    def __str__(self):
        s = ""
        for y in range(self.width):
            for x in range(self.height):
                i = self._to_index(x, y)
                s += str(self.grid[i])
            s += '\n'
        return s

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def get_total_path_cost(self, path):
        total = 0
        for p in path[1:]:
            total += self.grid[p]
        return total

    def get_path(self, start, end, h_func):
        open_set = [start]
        came_from = {}
        g_score = {i:sys.maxsize for i in range(self.width * self.height)}
        g_score[start] = 0
        
        f_score = {i:sys.maxsize for i in range(self.width * self.height)}
        sx, sy = self._from_index(start)
        ex, ey = self._from_index(end)
        f_score[start] = h_func(self, start, end)

        while len(open_set) > 0:
            current = open_set.pop()
            if current == end:
                return self.reconstruct_path(came_from, current)
            
            cx, cy = self._from_index(current)
            adjacent_indices = [(-1,0), (1, 0), (0, -1), (0, 1)]
            for adj in adjacent_indices:
                x, y = cx + adj[0], cy + adj[1]
                if x >= 0 and x < self.width and y >= 0 and y < self.height:
                    neighbour_index = self._to_index(x, y)
                    neighbour_g_score = g_score[current] + self.grid[neighbour_index]
                    if neighbour_g_score < g_score[neighbour_index]:
                        came_from[neighbour_index] = current
                        g_score[neighbour_index] = neighbour_g_score
                        f = neighbour_g_score + h_func(self, neighbour_index, end)
                        f_score[neighbour_index] = f
                        if neighbour_index not in open_set:
                            open_set.append(neighbour_index)
                            open_set.sort(key=lambda i: f_score[i], reverse=True)
        return []
    
    def extend_cavern(self):
        new_grid = [0] * self.width * 5  * self.height * 5
        for i in range(self.width * self.height):
            val = self.grid[i]
            x, y = self._from_index(i)

            for yc in range(0,5):
                for xc in range(0,5):
                    nx = xc * self.width + x
                    ny = yc * self.height + y

                    ni = ny * (self.width * 5) + nx
                    new_val = val + yc + xc
                    if new_val > 9:
                        new_val -= 9
                    new_grid[ni] = new_val
        
        self.width = self.width * 5
        self.height = self.height * 5
        self.grid = new_grid

def h_simple(map, start, end):
    sx, sy = map._from_index(start)
    ex, ey = map._from_index(end)
    return (ex-sx) + (ey-sy)

def main():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        cavern = Map(lines)
        path = cavern.get_path(0, (cavern.width*cavern.height)-1, h_simple)
        print(cavern.get_total_path_cost(path))
        
        cavern.extend_cavern()
        path = cavern.get_path(0, (cavern.width*cavern.height)-1, h_simple)
        print(cavern.get_total_path_cost(path))
        
main()