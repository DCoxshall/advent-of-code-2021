from math import inf

input_file = open("day7_input.txt", "r")
POSITIONS = [int(x) for x in input_file.readline().split(",")]

# === Part 1 ===

smallest = inf
for pos in range(len(POSITIONS)):
    cost = sum([abs(x - pos) for x in POSITIONS])
    if cost < smallest:
        smallest = cost
print(smallest)

# === Part 2 ###


def sum_to_n(n):
    return (n * (n+1))/2


smallest = inf
for pos in range(len(POSITIONS)):
    cost = sum([sum_to_n(abs(x - pos)) for x in POSITIONS])
    if cost < smallest:
        smallest = cost
print(smallest)
