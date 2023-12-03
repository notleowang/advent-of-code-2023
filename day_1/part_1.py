import re

def solve(lines):
    sum = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        calibration_value = digits[0] + digits[-1]
        sum += int(calibration_value)
    print(f"Sum of calibration values for part 1: {sum}")