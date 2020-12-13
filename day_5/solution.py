import math


def split_string(char_str):
    split_index = None

    for index, char in enumerate(char_str):
        if char in {'R', 'L'}:
            split_index = index

            break

    return (char_str[:split_index], char_str[split_index:])


def get_number_from_binary(chars, char_left_half, char_right_half):
    left = 0
    right = 2**len(chars) - 1

    for char in chars:
        diff = math.ceil((right - left) / 2)

        if char == char_left_half:
            right = right - diff
        elif char == char_right_half:
            left = left + diff

    return int(left)


def get_seat_info(char_str):
    row_str, column_str = split_string(char_str)

    row_number = get_number_from_binary(row_str, 'F', 'B')
    col_number = get_number_from_binary(column_str, 'L', 'R')
    seat_id = row_number * 8 + col_number

    return (row_number, col_number, seat_id)


def read_and_parse_lines(file_path):
    with open(file_path, 'r') as input:
        return [line.rstrip() for line in input.readlines()]


input = read_and_parse_lines('input.txt')

seat_ids = [get_seat_info(line)[2] for line in input]

print(max(seat_ids))
