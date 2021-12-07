import math

def sum_fuel_spent(positions, align_func, sum_func):
    positions.sort()
    fuel = 0
    align_to = align_func(positions)
    for pos in positions:
        fuel += sum_func(pos, align_to)
    return fuel

def part1_align(positions):
    return positions[len(positions)//2]

def part1_sum(position, align_to):
    return abs(position - align_to)

def part2_align(positions):
    return math.ceil(sum(positions)//len(positions))

def part2_sum(position, align_to):
    diff = abs(position - align_to)
    return diff * (diff+1) // 2

with open('input.txt') as input_file:
    input_text = input_file.readline()
    horizontal_positions = [int(x) for x in input_text.split(',')]
    print(sum_fuel_spent(horizontal_positions, part1_align, part1_sum))
    print(sum_fuel_spent(horizontal_positions, part2_align, part2_sum))