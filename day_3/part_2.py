# just some data structure (list) to store digits
digits = ["0", "1", "2", "3", "4", "4", "5", "6", "7", "8", "9"]

# indices of the * symbol
# - list of tuples: [(col_idx, row_idx), ...]
symbol_indices = []

# map of every part number and every col index + row index it appears in (0-based indexing)
# - For an 'n' digit part_number: [[(col_idx, row_idx), (col_idx, row_idx), ...], [(...), ...], ...]
part_numbers = {}


# helper for combining digits
def combine_digits(digits):
    return "".join(digits)


# initialize dictionary for part_numbers
def init_part_numbers(lines):
    # iterate through each line in the input file
    curr_row = 0
    for line in lines:
        curr_col = 0

        part_num_digits = []
        part_num_indices = [] # indices for each digit in part_number
        for i, symbol in enumerate(line):
            if symbol in digits:
                indices = (curr_col, curr_row)
                part_num_digits.append(symbol)
                part_num_indices.append(indices)

            # check if symbol is not a digit or on the last column
            if i >= len(line) - 1 or symbol not in digits:
                if part_num_digits:
                    part_num = combine_digits(part_num_digits)
                    if part_num in part_numbers.keys():
                        part_numbers[part_num].append(part_num_indices)
                        part_num_digits = []
                        part_num_indices = []
                    else:
                        part_numbers[part_num] = [part_num_indices]
                        part_num_digits = []
                        part_num_indices = []

            curr_col += 1
        curr_row += 1


# initialize list of all the indices where there is a '*' symbol
def init_symbols(lines):
    curr_row = 0

    for line in lines:
        curr_col = 0

        for symbol in line:
            if symbol == "*":
                indices = (curr_col, curr_row)
                symbol_indices.append(indices)
            curr_col += 1
        curr_row += 1


# get indices for left neighbours
def get_left_neighbours(col_idx, row_idx):
    top_left  = (col_idx - 1, row_idx - 1)
    left      = (col_idx - 1, row_idx)
    bot_left  = (col_idx - 1, row_idx + 1)
    return [top_left, left, bot_left]


# get indices for top and bottom neighbours
def get_top_bot_neighbours(col_idx, row_idx):
    top       = (col_idx,     row_idx - 1)
    bot       = (col_idx,     row_idx + 1)
    return [top, bot]


# get indices for right neighbours
def get_right_neighbours(col_idx, row_idx):
    top_right = (col_idx + 1, row_idx - 1)
    right     = (col_idx + 1, row_idx)
    bot_right = (col_idx + 1, row_idx + 1)
    return [top_right, right, bot_right]


# get the neighbouring indices around the symbol
# - assumption: no two gears can be beside eachother (i.e, '**')
def get_neighbours():
    neighbours = []

    for idx in symbol_indices:
        col_idx = idx[0]
        row_idx = idx[1]
        left = get_left_neighbours(col_idx, row_idx)
        top_bot = get_top_bot_neighbours(col_idx, row_idx)
        right = get_right_neighbours(col_idx, row_idx)
        neighbours += [left + top_bot + right]

    return neighbours


def solve(lines):
    sum = 0
    init_symbols(lines)
    init_part_numbers(lines)

    # get neighbours for every symbol index
    neighbours = get_neighbours()

    # check if there exists exactly two part numbers in neighbouring indices
    for n_indices in neighbours:
        # print(n_indices)
        gear_part_numbers = []
        gear_ratio = 0
        for part_number in part_numbers:
            for part_num_indices in part_numbers[part_number]:
                # print(part_num_indices)
                for part_num_index in part_num_indices:
                    if part_num_index in n_indices:
                        gear_part_numbers.append(int(part_number))
                        # print(gear_part_numbers)
                        break # breaks out of for loop so we don't re-add the same part number
        # print("---")

        if len(gear_part_numbers) == 2:
            gear_ratio = gear_part_numbers[0] * gear_part_numbers[1]

        sum += gear_ratio


    print(f"Sum of all the gears ratios in the engine schematic: {sum}")