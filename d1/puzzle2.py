# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# Advent of code 2023 day 1 part 2

input_text = open("input.txt").read().strip()
total_sum = 0

for line in input_text.split('\n'):
    extracted_digits = []

    for index, char in enumerate(line):
        if char.isdigit():
            extracted_digits.append(char)

        digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for digit, word in enumerate(digit_words):
            if line[index:].startswith(word):
                extracted_digits.append(str(digit + 1))
                break 
            
    if extracted_digits:
        total_sum += int(extracted_digits[0] + extracted_digits[-1])

print(total_sum)
