from collections import defaultdict

def parse_line(line):
    """Parse a line and return a dictionary of color counts."""
    _, events = line.split(':')
    color_counts = defaultdict(int)
    for event in events.split(';'):
        for balls in event.split(','):
            count, color = map(str.strip, balls.split())
            count = int(count)
            color_counts[color] = max(color_counts[color], count)
    return color_counts

def calculate_score(color_counts):
    """Calculate the score based on color counts."""
    score = 1
    for count in color_counts.values():
        score *= count
    return score

def process_file_for_p2(file_path):
    """Process the file and calculate p2."""
    with open(file_path) as file:
        lines = file.read().strip().split('\n')

    total_score = 0

    for line in lines:
        color_counts = parse_line(line)
        total_score += calculate_score(color_counts)

    return total_score

file_path = 'input.txt'
answer = process_file_for_p2(file_path)
print(answer)
