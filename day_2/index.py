from functions import get_count_with_limits, get_count_with_positions

parsed_values = []

with open('input.txt', 'r') as input:
    for line in input.readlines():
        numbers, match_letter, code = line.split(' ')

        low_number, high_number = map(lambda x: int(x), numbers.split('-'))
        match_letter = match_letter[:-1]
        code = code.rstrip()

        parsed_values.append({
            'low_number': low_number,
            'high_number': high_number,
            'match_letter': match_letter,
            'code': code,
        })


print(get_count_with_limits(parsed_values))
print(get_count_with_positions(parsed_values))
