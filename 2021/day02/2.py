import os
sample = False

filename = ""
if sample:
    filename = "sample.txt"
else:
    filename = "input.txt"

commands = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, filename),) as file:
    commands = file.readlines()

def parse_command(command):
    tokens = command.split(" ")
    return tokens[0], int(tokens[1])

# Part 1
forward = 0
depth = 0
for command in commands:
    direction, value = parse_command(command)

    if direction == "forward":
        forward += value
    elif direction == "down":
        depth += value
    else:
        depth -= value
    
print(forward * depth)

# Part 2
forward = 0
depth = 0
aim = 0
for command in commands:
    direction, value = parse_command(command)

    if direction == "forward":
        forward += value
        depth += aim * value
    elif direction == "down":
        aim += value
    else:
        aim -= value
    
print(forward * depth)