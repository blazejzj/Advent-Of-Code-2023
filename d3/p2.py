from collections import defaultdict

def parse_grid_for_second_sum(grid):
    gear_nums = defaultdict(list)
    
    for r, row in enumerate(grid):
        number, gears = 0, set()

        for c, char in enumerate(row + [' ']):
            if char.isdigit():
                number = number * 10 + int(char)
                update_gears(r, c, gears, grid)
            elif number > 0:
                for gear in gears:
                    gear_nums[gear].append(number)
                number, gears = 0, set()

    return calculate_second_sum(gear_nums)

def update_gears(row, col, gears, grid):
    for rr in range(row - 1, row + 2):
        for cc in range(col - 1, col + 2):
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                if grid[rr][cc] == '*':
                    gears.add((rr, cc))

def calculate_second_sum(gear_nums):
    second_sum = 0
    for nums in gear_nums.values():
        if len(nums) == 2:
            second_sum += nums[0] * nums[1]
    return second_sum

# Read the grid from the file and parse it for second sum
grid = [list(line.strip()) for line in open('input.txt').readlines()]
second_sum = parse_grid_for_second_sum(grid)

print("Second Sum:", second_sum)
