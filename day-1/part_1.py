import re

def solve(lines):
    sum = 0
    for line in lines:
        digits = re.findall("\d", line)
        calibration_value = digits[0] + digits[-1]
        sum += int(calibration_value)
    print(f"Part 1: Sum of calibration values: {sum}")