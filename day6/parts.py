
def generate_day_counts(input_list):
    day_counts = [0] * 9
    for day in input_list:
        day_counts[day] += 1
    return day_counts

def calculate_next_day_counts(current_counts):
    new_counts = [0] * 9

    new_counts[0] = current_counts[1]
    new_counts[1] = current_counts[2]
    new_counts[2] = current_counts[3]
    new_counts[3] = current_counts[4]
    new_counts[4] = current_counts[5]
    new_counts[5] = current_counts[6]
    new_counts[6] = current_counts[7] + current_counts[0]
    new_counts[7] = current_counts[8]
    new_counts[8] = current_counts[0]

    return new_counts

def run_simulation(day_counts, num_days):
    for day in range(num_days):
        day_counts = calculate_next_day_counts(day_counts)
    return sum(day_counts)
    

def main():
    with open('input.txt') as input_file:
        day_counts = generate_day_counts([int(x) for x in input_file.readline().split(',')])
        print(f"After 80 days there are {run_simulation(day_counts, 80)}")
        print(f"After 256 days there are {run_simulation(day_counts, 256)}")

if __name__ == '__main__':
    main()