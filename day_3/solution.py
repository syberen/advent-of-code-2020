def read_and_parse_lines(file_path):
    with open(file_path, 'r') as input:
        return [line.rstrip() for line in input.readlines()]


input = read_and_parse_lines('input.txt')


def count_encountered_trees(input, right, down):
    grid = [[char for char in line] for line in input]
    grid_length = len(grid)
    grid_width = len(grid[0])

    pos_x = 0
    count = 0

    for i in range(0, grid_length, down):
        if grid[i][pos_x % grid_width] == '#':
            count += 1

        pos_x += right

    return count


# Part 1 solution
print(count_encountered_trees(input, 3, 1))

# Part 2 solution
a = count_encountered_trees(input, 1, 1)
b = count_encountered_trees(input, 3, 1)
c = count_encountered_trees(input, 5, 1)
d = count_encountered_trees(input, 7, 1)
e = count_encountered_trees(input, 1, 2)

print(a * b * c * d * e)
