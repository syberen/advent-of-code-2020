def count_unique_group_answers(input):
    group_chunks = input.split('\n\n')

    count = 0

    for chunk in group_chunks:
        group_string = chunk.replace('\n', '')
        group_set = set([char for char in group_string])

        count += len(group_set)

    return count


def count_unanimous_group_answers(input):
    group_chunks = input.split('\n\n')

    count = 0

    for chunk in group_chunks:
        individual_answers = [set([char for char in char_str])
                              for char_str in chunk.split('\n')]

        common_answers = set.intersection(*individual_answers)

        count += len(common_answers)

    return count


with open('input.txt', 'r') as file:
    input = file.read()

    # Part 1 answer
    print(count_unique_group_answers(input))

    # Part 2 answer
    print(count_unanimous_group_answers(input))
