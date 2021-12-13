def load_data():
    with open('input.txt') as input_file:
        folds = []
        coords = []
        for line in input_file:
            if line == '\n':
                continue
            if line.startswith('fold along'):
                fold = line.split()[2].split('=')
                fold[1] = int(fold[1])
                folds.append(fold)
            else:
                coords.append(tuple([int(x) for x in line.rstrip().split(',')]))
    return coords, folds

def process_data(coords, folds):
    for fold in folds:
        axis, pos = fold
        new_coords = []
        for coord in coords:
            x, y = coord
            if (axis == 'y' and y < pos) or (axis == 'x' and x < pos):
                if coord not in new_coords:
                    new_coords.append(coord)
                continue
            
            if axis == 'y':
                y = pos - (y - pos)
            elif axis == 'x':
                x = pos - (x - pos)
                
            new_coord = (x, y)
            if new_coord not in new_coords:
                new_coords.append(new_coord)
        coords = new_coords
    return coords

def print_data(coords):
    max_x = max(coords, key=lambda c: c[0])[0]
    max_y = max(coords, key=lambda c: c[1])[1]
    canvas = [' ' * (max_x + 1)] * (max_y + 1)
    for c in coords:
        x, y = c
        canvas[y] = canvas[y][:x] + 'x' + canvas[y][x+1:]
    for row in canvas:
        print(row)


def main():
    coords, folds = load_data()
    print(f"After one fold, there are {len(process_data(coords, folds[:1]))} points")
    print_data(process_data(coords, folds))
    
main()