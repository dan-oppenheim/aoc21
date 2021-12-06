
def generate_day_counts(input_list):
    day_counts = [0] * 9
    for day in input_list:
        day_counts[day] += 1
    return day_counts

def calculate_next_day_counts(current_counts):
    new_counts = current_counts[1:] # move all fish down a day
    new_counts.append(current_counts[0]) # add new fish
    new_counts[6] += current_counts[0] # move fish at day zero to day 6
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