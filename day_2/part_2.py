import re
import sys

def solve(lines):
    sum = 0

    # iterate through each game
    for line in lines:
        r_max, g_max, b_max = 0, 0, 0

        sets = line.split(";")

        # print("\nNew game")

        # iterate through each "round" in a game
        for subset in sets:
            r_match = re.findall(r"(\d+) red", subset)
            g_match = re.findall(r"(\d+) green", subset)
            b_match = re.findall(r"(\d+) blue", subset)

            r_cubes = int(r_match[0]) if r_match else 0
            g_cubes = int(g_match[0]) if g_match else 0
            b_cubes = int(b_match[0]) if b_match else 0

            # print(f"Red: {r_cubes}, Green: {g_cubes}, Blue: {b_cubes}")

            # check if any of the cube amounts are larger than current maximums
            # - if larger, update maxes
            if r_cubes > r_max: r_max = r_cubes
            if g_cubes > g_max: g_max = g_cubes
            if b_cubes > b_max: b_max = b_cubes

        # print(f"r_max: {r_max}, g_max: {g_max}, b_max: {b_max}")

        power = r_max * g_max * b_max
        # print(f"Power: {power}")

        sum += power

    print(f"Sum of Powers: {sum}")