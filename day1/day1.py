
with open('day1_input.txt') as inputfile:
    current_reading = int(inputfile.readline())
    larger_count = 0
    for line in inputfile:
        reading = int(line)

        if reading > current_reading:
            larger_count += 1
        current_reading = reading

    print(larger_count)
        
        