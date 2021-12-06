
# For each bit, count the number of positive bits. Then build a new list,
# populated with those bit strings that match the critera.

# Move on to the next bit and repeat this process until the new list has only
# a single bit string in it. That string is the rating.


def calculate_bit_occurrences(binary_strings, bit):
    bit_count = 0
    for binary_string in binary_strings:
        if binary_string[bit] == '1':
            bit_count += 1
    return bit_count

def calculate_rating(binary_strings, num_bits, keep_test):
    num_strings = len(binary_strings)

    for i in range(num_bits):
        bit_count = calculate_bit_occurrences(binary_strings, i)
        binary_strings = [
            bs for bs in binary_strings 
                if keep_test(bit_count, bs[i], len(binary_strings))
        ]
        if len(binary_strings) == 1:
            break
    
    return int('0b' + ''.join(binary_strings[0]), base=2)

def oxygen_keep_test(count, digit, num_strings):
    if count >= (num_strings + 1) // 2:
        return digit == '1'
    else:
        return digit == '0'

def co2_scrubber_keep_test(count, digit, num_strings):
    return not oxygen_keep_test(count, digit, num_strings)

with open('input.txt') as input_file:
    binary_strings = [x for x in input_file]
    oxygen_rating = calculate_rating(binary_strings, 12, oxygen_keep_test)
    co2_rating = calculate_rating(binary_strings, 12, co2_scrubber_keep_test)

    print(oxygen_rating * co2_rating)
    