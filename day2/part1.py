with open('part1_input.txt') as input_filename:
    horizontal_position = 0
    depth = 0

    for line in input_filename:
        direction, value = line.split()
        match direction:
            case 'forward':
                horizontal_position += int(value)
            case 'up':
                depth -= int(value)
            case 'down':
                depth += int(value)

    print(horizontal_position * depth)