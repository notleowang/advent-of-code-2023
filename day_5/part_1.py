'''
Dictionary to store a specific map with the following structure:
KEY | VALUE
-----------
 id | list of ranges

'''
maps = {}

'''
Class to store a range for a specific map.
- The range class will store the "start" and "end" for a destination and source range.

'''
class range:
    destination_range_start = 0
    destination_range_end = 0
    source_range_start = 0
    source_range_end = 0

    def __init__(self, dest, source, length):
        self.destination_range_start = dest
        self.source_range_start = source

        self.destination_range_end = dest + length - 1
        self.source_range_end = source + length - 1

    def get_destination(self, seed):
        offset = self.source_range_start - seed
        print(offset)

        return 0


# helper function to initialize the maps dictionary and seeds list
def init_maps_and_seeds(lines):
    seeds = []

    isMap = False
    id = -1
    curr_ranges = []

    for i, line in enumerate(lines):

        # should be the seeds to be planted
        if i == 0:
            seeds = line.split(" ")
            seeds.pop(0)
            seeds = [int(i) for i in seeds]

        # if empty line in almanac, then we finished adding ranges for a corresponding map
        # so set isMap to false
        if line == "" and isMap:
            isMap = False
            continue

        # should be iterating inside a map if isMap is true
        if isMap:
            print(line)
            range_nums = line.split(" ")
            curr_range = range(int(range_nums[0]), int(range_nums[1]), int(range_nums[2]))
            curr_ranges.append(curr_range)

        # check if next line is gonna be the start of a map in the almanac
        if "map" in line:
            id += 1
            maps[id] = curr_ranges
            curr_ranges = []
            isMap = True

    return seeds


# helper function to check if a seed is between given range
def is_between(seed, range):
    minimum = range.source_range_start
    maximum = range.source_range_end

    if minimum <= seed <= maximum:
        return True

    return False


def solve(lines):
    seeds = init_maps_and_seeds(lines)

    print("----")
    print(maps)

    # for each seed, we will...
    for seed in seeds:

        # ...traverse through each map saving the "current destination" until we finish iterating through
        curr_dest = seed
        for key, ranges in maps.items():
            for curr_range in ranges:
                # if we find a range that the seed sits between,
                # - overwrite curr_dest
                # else, curr_dest should just be the seed number
                if (is_between(curr_dest, curr_range)):
                    curr_dest = curr_range.get_destination(curr_dest)
                    continue

            # if we're at the end, we save the final destination (which should
            # be a number corresponding to the location of a seed)

            if key == list(maps)[-1]:
                print("done")

        break