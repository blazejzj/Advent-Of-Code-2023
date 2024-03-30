from collections import defaultdict

def parse_line(line):
    """Parse a line and return the id and a dictionary of color counts."""
    id_, events = line.split(':')
    color_counts = defaultdict(int)
    for event in events.split(';'):
        for balls in event.split(','):
            count, color = map(str.strip, balls.split())
            count = int(count)
            color_counts[color] = max(color_counts[color], count)
    return id_, color_counts

def process_file_for_p1(file_path):
    """Process the file and calculate p1."""
    with open(file_path) as file:
        lines = file.read().strip().split('\n')

    total_valid_id = 0
    color_limits = {'red': 12, 'green': 13, 'blue': 14}

    for line in lines:
        id_, color_counts = parse_line(line)
        if all(count <= color_limits.get(color, float('inf')) for color, count in color_counts.items()):
            total_valid_id += int(id_.split()[-1])

    return total_valid_id

file_path = 'input.txt'
answer = process_file_for_p1(file_path)
print(answer)