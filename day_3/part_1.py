"""
Visualization of indices (col, row):
(0, 0) | (1, 0) | (2, 0)
(0, 1) | (1, 1) | (2, 1)
(0, 2) | (1, 2) | (2, 2)

Visualization of Part Number with one digit:
X | X | X
X | O | X
X | X | X

Visualization of Part Number with > than one digit:
X | X | X | X | X
X | O   O   O | X
X | X | X | X | X

Visualization with indices (one digit): 
(col_idx - 1, row_idx - 1) | (col_idx    , row_idx - 1) | (col_idx + 1, row_idx - 1)
(col_idx - 1, row_idx    ) |        part_number         | (col_idx + 1, row_idx    )
(col_idx - 1, row_idx + 1) | (col_idx    , row_idx + 1) | (col_idx + 1, row_idx + 1)

Q: Why don't I use the index() function to get index instead of "curr counters"?
A: The index() function only gets the index of the first occurence. That means if a duplicate
   symbol/number shows up, there's some issues.

"""

# just some data structure (list) to store digits
digits = ["0", "1", "2", "3", "4", "4", "5", "6", "7", "8", "9"]

# map of a symbol and every col index + row index it appears in (0-based indexing)
# - symbol: [(col_idx, row_idx), (col_idx, row_idx), ...]
symbols = {}

# map of every part number and every col index + row index it appears in (0-based indexing)
# - For an 'n' digit part_number: [[(col_idx, row_idx), (col_idx, row_idx), ...], [(...), ...], ...]
part_numbers = {}


# helper for combining digits
def combine_digits(digits):
    return "".join(digits)


# initialize dictionary for symbols
def init_symbols(lines):
    curr_row = 0

    for line in lines:
        curr_col = 0

        for symbol in line:
            if symbol in digits or symbol == ".":
                curr_col += 1
                continue

            indices = (curr_col, curr_row)
            if symbol in symbols.keys():
                symbols[symbol].append(indices)
            else:
                symbols[symbol] = [indices]

            curr_col += 1
        curr_row += 1


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


# get the neighbouring indices around the part number
def get_neighbours(part_num_indices):
    neighbours = []

    # check if the part number is just one digit
    if len(part_num_indices) == 1:
        part_num = part_num_indices[0]
        col_idx = part_num[0]
        row_idx = part_num[1]
        left = get_left_neighbours(col_idx, row_idx)
        top_bot = get_top_bot_neighbours(col_idx, row_idx)
        right = get_right_neighbours(col_idx, row_idx)
        neighbours = left + top_bot + right
    else:
        for idx in part_num_indices:
            temp_neighbours = []
            col_idx = idx[0]
            row_idx = idx[1]
            
            # check if we're on the first digit of the part number
            digit_idx = part_num_indices.index(idx)
            if digit_idx == 0:
                left = get_left_neighbours(col_idx, row_idx)
                top_bot = get_top_bot_neighbours(col_idx, row_idx)
                temp_neighbours = left + top_bot
            # check if we're on the last digit of the part number
            elif digit_idx == len(part_num_indices) - 1:
                right = get_right_neighbours(col_idx, row_idx)
                top_bot = get_top_bot_neighbours(col_idx, row_idx)
                temp_neighbours = right + top_bot
            else:
                temp_neighbours = get_top_bot_neighbours(col_idx, row_idx)
            
            neighbours += temp_neighbours
    
    return neighbours


# checks if part number is adjacent to a symbol
# - check if a symbol exists in one of the neighbouring indices
def is_adjacent(neighbours):
    for symbol in symbols:
        for s_idx in symbols[symbol]:
            if s_idx in neighbours:
                # print(neighbours)
                # print(s_idx)
                return True
    return False
        

def solve(lines):
    sum = 0

    init_symbols(lines)
    init_part_numbers(lines)
    
    # iterate through each part number
    for part_number in part_numbers:
        # print(part_number)
        
        # iterate through each list of indices for the given part number's digits
        for part_num_indices in part_numbers[part_number]:
            
            # get list of "neighbours" for each digit in the part number
            neighbours = get_neighbours(part_num_indices)
            # print(neighbours)
            if is_adjacent(neighbours):
                sum += int(part_number)
                # print(sum)

        # print("------")

    print(f"Sum of all the part numbers in the engine schematic: {sum}")