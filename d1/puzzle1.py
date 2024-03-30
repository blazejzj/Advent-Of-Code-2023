# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently 
# just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number

# Advent of code 2023 day 1

with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    digits = []
    first_digit = None
    last_digit = None
    for word in data:
        for char in word:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                last_digit = char
        digits.append(first_digit + last_digit)
        first_digit = None
        last_digit = None
    sum = 0
    for digit in digits:
        sum += int(digit)
    print(sum)
