import os
sample = False

filename = ""
if sample:
    filename = "sample.txt"
else:
    filename = "input.txt"

readings = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, filename),) as file:
    readings = file.readlines()
    readings = [reading.rstrip() for reading in readings]


def process_readings(readings):
    readings_2d = []
    for reading in readings:
        readings_2d.append(split(reading))
    
    return readings_2d

def print_2d_list(list_2d):
    for r in list_2d:
        for c in r:
            print(c, end = " ")
        print()

def split(s):
    return [char for char in s]

def unsplit(lst):
    return "".join(lst)

def get_most_frequent_bit_in_row(list_2d, r):
    return get_most_frequent_bit(list_2d[r])

def get_most_frequent_bit_in_col(list_2d, c):
    return get_most_frequent_bit([elem[c] for elem in list_2d])

def get_most_frequent_bit(bits):
    return "1" if bits.count("1") >= (len(bits)/2) else "0"

def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n

def get_gamma(list_2d, as_str=True):
    gamma = ""
    for c in range(len(list_2d[0])):
        gamma += get_most_frequent_bit_in_col(list_2d, c)
    return gamma


# Part 1
num_cols = len(readings[0])
readings_2d = process_readings(readings)

gamma = get_gamma(readings_2d)
gamma = int(gamma, base=2)
epsilon = bit_not(gamma, numbits=num_cols)

print(gamma * epsilon)



# Part 2
remaining_readings = readings_2d
for c in range(num_cols):
    gamma_val = get_most_frequent_bit_in_col(remaining_readings, c)
    remaining_readings = [reading for reading in remaining_readings if reading[c] == gamma_val]

    if len(remaining_readings) == 1:
        break

o2 = unsplit(remaining_readings[0])
    

remaining_readings = readings_2d
for c in range(num_cols):
    gamma_val = "0" if get_most_frequent_bit_in_col(remaining_readings, c) == "1" else "1"
    remaining_readings = [reading for reading in remaining_readings if reading[c] == gamma_val]
    
    if len(remaining_readings) == 1:
        break

co2 = unsplit(remaining_readings[0])

o2  = int(o2, base=2)
co2 = int(co2, base=2)

print(o2 * co2)