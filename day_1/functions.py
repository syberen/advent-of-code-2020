def find_pair(values, amount):
    values_set = set(values)

    for value in values_set:
        match = amount - value

        if match in values_set:
            return {value, match}


def find_triplet(values, amount):
    for value in values:
        matching_total = amount - value

        matching_tuple = find_pair(values, matching_total)

        if matching_tuple is not None:
            a, b = matching_tuple

            return {a, b, value}
