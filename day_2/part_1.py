import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def solve(lines):
    sum = 0

    # iterate through each game
    for line in lines:
        game_id = re.search(r"Game (\d+)", line).group(1)
        valid = 1

        sets = line.split(";")

        # print(f"\nGame {int(game_id)}:")

        # iterate through each "round" in a game
        for subset in sets:
            r_match = re.findall(r"(\d+) red", subset)
            g_match = re.findall(r"(\d+) green", subset)
            b_match = re.findall(r"(\d+) blue", subset)

            r_cubes = int(r_match[0]) if r_match else 0
            g_cubes = int(g_match[0]) if g_match else 0
            b_cubes = int(b_match[0]) if b_match else 0

            # print(f"Red: {r_cubes}, Green: {g_cubes}, Blue: {b_cubes}")

            # check if any of the cube amounts are bigger than bag's amounts
            # - if larger, then we know this subset is impossible
            if  (r_cubes > bag["red"]     or
                g_cubes > bag["green"]    or
                b_cubes > bag["blue"]):
                valid = 0
                break

         # if an invalid subset was found then just skip game
        if not valid:
            continue

        sum += int(game_id) if valid else 0

    print(f"Sum of Game IDs: {sum}")