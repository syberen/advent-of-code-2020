def get_count_with_limits(values):
    valid_count = 0

    for value in values:
        letter_count = 0

        for letter in value['code']:
            if letter == value['match_letter']:
                letter_count += 1

        if value['low_number'] <= letter_count <= value['high_number']:
            valid_count += 1

    return valid_count


def get_count_with_positions(values):
    valid_count = 0

    for value in values:
        low_index = value['low_number'] - 1
        high_index = value['high_number'] - 1

        code = value['code']

        low_match = code[low_index] == value['match_letter']
        high_match = code[high_index] == value['match_letter']

        if (low_match and not high_match) or (not low_match and high_match):
            valid_count += 1

    return valid_count
