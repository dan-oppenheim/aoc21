pairs = {
    ']': '[',
    '}': '{',
    ')': '(',
    '>': '<'
}

def check_line(line):
    stack = []
    for c in line:
        if c in pairs.values():
            stack.append(c)
        else:
            top = stack.pop()
            if top != pairs[c]:
                return False, c
    return True, None

def get_completed_line_score(line):
    stack = []
    for c in line:
        if c in pairs.values():
            stack.append(c)
        else:
            stack.pop() 

    total = 0
    while len(stack) > 0:
        c = stack.pop()
        total *= 5
        match c:
            case '(': total += 1
            case '[': total += 2
            case '{': total += 3
            case '<': total += 4
    return total



def process_input(input_lines):
    completed_line_scores = []
    count = 0
    for line in input_lines:
        line = line.strip()
        ok, c = check_line(line)
        if not ok:
            match c:
                case ')':
                    count += 3
                case ']':
                    count += 57
                case '}':
                    count += 1197
                case '>':
                    count += 25137
        else:
            completed_line_scores.append(get_completed_line_score(line))
        
    print(count)
    completed_line_scores.sort()
    print(completed_line_scores[len(completed_line_scores)//2])

with open('input.txt') as input_file:
    lines = input_file.readlines()
    process_input(lines)