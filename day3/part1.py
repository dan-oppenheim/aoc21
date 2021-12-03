
def calculate_gamma(input_file, bit_length):
    bit_state_count = [0] * bit_length
    for line in input_file:
        for i in range(bit_length):
            bit_state_count[i] += 1 if line[i] == '1' else -1
    
    return ''.join(['1' if int(x) > 0 else '0' for x in bit_state_count])
    

with open('input.txt') as input_file:
    gamma = calculate_gamma(input_file, 12)
    epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])

    print(int('0b' + gamma, base=2) * int('0b' + epsilon, base=2))






        