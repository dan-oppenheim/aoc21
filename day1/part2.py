
# the test is always on four entries:
# 0 1 2 3 4
# a a a
#   b b b
#     c c c
#
# 1 1 1 1   <- first test
#   2 2 2 2 <= second test

# slide a list of four entries down the input, compare sums of 0:3 and 1:

with open('part2_input.txt') as input_file:
    # pre-populate to avoid logic in the loop
    window = [int(next(input_file)) for x in range(4)]

    increase_count = 1 if sum(window[1:]) > sum(window[0:3]) else 0

    for line in input_file:
        window = window[1:]
        window.append(int(line))

        if sum(window[1:]) > sum(window[0:3]):
            increase_count += 1

    print(increase_count)