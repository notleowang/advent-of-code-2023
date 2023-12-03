import re

def solve(lines):
    map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    sum = 0
    for line in lines:
        digits = []
        groups = re.findall(r"(?=(one))|(?=(two))|(?=(three))|(?=(four))|(?=(five))|(?=(six))|(?=(seven))|(?=(eight))|(?=(nine))|(\d)", line)
        for group in groups:
            group = list(filter(None, group))
            digits.append(group[0])

        if (digits[0] in map):
            first_digit = map[digits[0]]
        else:
            first_digit = digits[0]

        if (digits[-1] in map):
            second_digit = map[digits[-1]]
        else:
            second_digit = digits[-1]

        calibration_value = first_digit + second_digit

        sum += int(calibration_value)
    print(f"Sum of calibration values for part 2: {sum}")