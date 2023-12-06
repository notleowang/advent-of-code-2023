import re

# helper
def split_scratch_card(scratch_card_numbers):
    list_of_nums = scratch_card_numbers.split("|")
    winning_nums = re.findall(r"\d+", list_of_nums[0])
    my_nums      = re.findall(r"\d+", list_of_nums[1])
    return winning_nums, my_nums

def solve(lines):
    sum = 0

    for line in lines:
        scratch_card_numbers = re.sub(r"Card\s*\d+:\s*", "", line)
        winning_numbers, my_numbers = split_scratch_card(scratch_card_numbers)

        count = 0
        for num in my_numbers:
            if num in winning_numbers:
                count += 1

        sum += 2 ** (count - 1) if count != 0 else 0

    print(sum)

"""
Pattern observed:

matches | points
----------------
    0   |   0
    1   |   1
    2   |   2
    3   |   4
    4   |   8
    .   |   .
    .   |   .
    .   |   .
    n   |   2 ** (n - 1), for n > 0

"""