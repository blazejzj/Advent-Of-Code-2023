from collections import defaultdict

def parse_grid_for_part_sum(grid):
    part_sum = 0
    
    for r, row in enumerate(grid):
        number, has_part = 0, False

        for c, char in enumerate(row + [' ']):
            if char.isdigit():
                number = number * 10 + int(char)
                has_part = check_adjacent_chars(r, c, grid, has_part)
            elif number > 0:
                if has_part:
                    part_sum += number
                number, has_part = 0, False

    return part_sum

def check_adjacent_chars(row, col, grid, has_part):
    for rr in range(row - 1, row + 2):
        for cc in range(col - 1, col + 2):
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                ch = grid[rr][cc]
                if not ch.isdigit() and ch != '.':
                    has_part = True
    return has_part

# Read the grid from the file and parse it for part 1 sum
grid = [list(line.strip()) for line in open('input.txt').readlines()]
part_sum = parse_grid_for_part_sum(grid)

print("Part 1 Sum:", part_sum)
