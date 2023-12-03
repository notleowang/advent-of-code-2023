import sys
import part_1, part_2

def read_file():
    file = open("input.txt", "r")
    return file.read().splitlines()

def main():
    args = sys.argv[1]
    lines = read_file()

    if len(args) == 0:
        print("No arguments given")
        return

    match args[0]:
        case "1":
            part_1.solve(lines)
        case "2":
            part_2.solve(lines)
        case "a":
            part_1.solve(lines)
            part_2.solve(lines)

if __name__ == "__main__":
    main()