import os

sample = False

filename = ""
if sample:
    filename = "sample.txt"
else:
    filename = "input.txt"

data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, filename),) as file:
    data = file.readlines()


def parse_range(range_str):
    tokens = range_str.split("-")
    return [int(tokens[0]), int(tokens[1])]

def parse_char(char_str):
    return char_str.replace(":", "")

def in_range(num, bounds):
    return num >= bounds[0] and num <= bounds[1]

def has_char_at(str, char, i):
    return str[i] == char

# Part 1
valid_passwords = 0
for str in data:
    tokens = str.split(" ")

    rng = parse_range(tokens[0])
    needle = parse_char(tokens[1])
    haystack = tokens[2]

    count = haystack.count(needle)

    if in_range(count, rng):
        valid_passwords += 1

print(valid_passwords)

# Part 2
valid_passwords = 0
for str in data:
    tokens = str.split(" ")

    rng = parse_range(tokens[0])
    needle = parse_char(tokens[1])
    haystack = tokens[2]

    if has_char_at(haystack, needle, rng[0] - 1) ^ has_char_at(haystack, needle, rng[1] - 1):
        valid_passwords += 1

print(valid_passwords)

