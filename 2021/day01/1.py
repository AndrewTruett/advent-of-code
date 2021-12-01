import os

def count_increases(data):
    increases = 0
    for i in range(0, len(data) - 1):
        if data[i + 1] > data[i]:
            increases += 1
    return increases

sample = False

filename = ""
if sample:
    filename = "sample.txt"
else:
    filename = "input.txt"

depths = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, filename),) as file:
    depths = file.readlines()
    depths = [int(depth.rstrip()) for depth in depths]



grouped_depths = []

upper_bound = 2
i = 0
while upper_bound < len(depths):
    sum = depths[i] + depths[i+1] + depths[i+2]
    grouped_depths.append(sum)
    i+=1
    upper_bound+=1

increases = count_increases(grouped_depths)
print(increases)    