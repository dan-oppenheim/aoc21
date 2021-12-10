test_data = [
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf",
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]


def process_part1(input_data):
    count = 0
    for line in input_data:
        first, second = line.split(' | ')
        outputs = second.split()
        for output in outputs:
            if len(output) in [2, 4, 3, 7]:
                count += 1
    print(count)

    

def process_part2(input_data):
    first, second = input_data.split(' | ')
    inputs = first.split()

    digits = [[] for x in range(10)]
    for i in inputs:
        i = ''.join(sorted(i))
        match len(i):
            case 2:
                digits[1] = i
            case 3:
                digits[7] = i
            case 4:
                digits[4] = i
            case 5:
                digits[2].append(i)
                digits[3].append(i)
                digits[5].append(i)
            case 6:
                digits[6].append(i)
                digits[9].append(i)
                digits[0].append(i)
            case 7:
                digits[8] = i

    scrambled_lut = {
        digits[1] : "cf",
        digits[4] : "bcdf",
        digits[7] : "acf",
        digits[8] : "abcdefg",
    }

    for d in digits[3]:
        if digits[1][0] in d and digits[1][1] in d:
            digits[3] = d
            scrambled_lut[d] = "acdfg"
            digits[2].remove(d)
            digits[5].remove(d)
            break

    for d in digits[6]:
        if digits[1][0] in d and digits[1][1] in d:
            continue # 0 or 9
        else:
            digits[6] = d
            scrambled_lut[d] = "abdefg"
            digits[9].remove(d)
            digits[0].remove(d)

    for d in digits[5]:
        diff = set(digits[6]).difference(d)
        if len(diff) == 1:
            digits[5] = d
            scrambled_lut[d] = "abdfg"
            if list(diff)[0] in digits[0][0]:
                digits[9].remove(digits[0][0])
                digits[9] = digits[9][0]
                digits[0] = digits[0][0]
                
            else:
                digits[9].remove(digits[0][1])
                digits[9] = digits[9][0]
                digits[0] = digits[0][1]
            scrambled_lut[digits[0]] = "abcefg"
            scrambled_lut[digits[9]] = "abcdfg"
        else:
            digits[2] = d
            scrambled_lut[d] = "acdeg"

    
    digit_lut = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9"
    }

    outputs = second.split()
    value = ""
    for output in outputs:
        s = ''.join(sorted(output))
        trans = scrambled_lut[s]
        value += digit_lut[trans]
    return int(value)

with open('input.txt') as input_file:
    entries = input_file.readlines()
    #process_part1(entries)
    total = 0
    for entry in entries:
        total += process_part2(entry)
    print(total)