with open('part1_input.txt') as input_filename:
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in input_filename:
        direction, value = line.split()
        match direction:
            case 'forward':
                horizontal_position += int(value)
                depth += aim * int(value)
            case 'up':
                aim -= int(value)
            case 'down':
                aim  += int(value)

    print(horizontal_position * depth)