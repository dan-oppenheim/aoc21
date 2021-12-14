def load_data(file_name):
    polymer_template = None
    insertion_rules = {}
    with open(file_name) as input_file:
        polymer_template = input_file.readline().strip()
        input_file.readline()
        for line in input_file.readlines():
            match_pair, insert_element = line.split(' -> ')
            insertion_rules[match_pair] = insert_element.rstrip()
    return polymer_template, insertion_rules

def polymer_to_pairs(polymer, insertion_rules):
    pairs = {pair:0 for pair in insertion_rules.keys()}
    for i in range(len(polymer)-1):
        pairs[polymer[i:i+2]] += 1
    return pairs

def process_polymer(pairs, insertion_rules):
    new_pairs = {pair:0 for pair in insertion_rules.keys()}
    for k, v in pairs.items():
        if v == 0:
            continue
        elem = insertion_rules[k]
        new_pairs[k[0] + elem] += v
        new_pairs[elem + k[1]] += v
    return new_pairs

def count_elems(pairs, keys):
    elems = {key:0 for key in keys}
    for k, v in pairs.items():
        elems[k[0]] += v
        elems[k[1]] += v
    return (min(elems.values()) + 1) // 2, (max(elems.values()) + 1) // 2

def main():
    polymer_template, insertion_rules = load_data('input.txt')
    pairs = polymer_to_pairs(polymer_template, insertion_rules) 
    for i in range(40):
        pairs = process_polymer(pairs, insertion_rules)

    # assume that there is at least one rule that produces each possible
    # new pair, so can just use the values as all possible elements
    min_count, max_count = count_elems(pairs, insertion_rules.values())
    print(max_count - min_count)

main()

        