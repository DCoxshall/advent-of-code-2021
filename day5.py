from copy import deepcopy

# Each line from input should be parsed into a list of lists, of the form [x1, y1, x2, y2]
input_file = open("day5_input.txt", "r")
lines = input_file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace(" -> ", ",")
    lines[i] = lines[i].replace("\n", "")
    lines[i] = [int(k) for k in lines[i].split(",")]
LINES = lines  # I know this isn't strictly necessary but it helps

lines = deepcopy(LINES)  # Get a copy of LINES which is safe to edit

# Cut out all lines where x1 == x2 or y1 == y2
# ATTENTION: Removing this line will produce the solution for Part 2. Leaving
# it in produces the solution for Part 1
lines = [line for line in lines if line[0] == line[2] or line[1] == line[3]]

# Get size of the grid based on the largest numbers in lines
side_length = max([x for sublist in lines for x in sublist]) + 1

# Inititalise square grid
grid = [[0 for _ in range(side_length)] for _ in range(side_length)]

# Paint the lines onto the grid
for line in lines:
    x1, y1, x2, y2 = line  # Unpack the line into coordinate variables
    tempX = x1
    tempY = y1
    grid[tempY][tempX] = grid[tempY][tempX] + 1
    while tempX != x2 or tempY != y2:
        if tempX < x2:
            tempX += 1
        if tempX > x2:
            tempX -= 1
        if tempY < y2:
            tempY += 1
        if tempY > y2:
            tempY -= 1
        grid[tempY][tempX] = grid[tempY][tempX] + 1


# Calculate the number of points in the grid which are greater than 1
total = 0
for i in grid:
    for j in i:
        if j > 1:
            total += 1

print(total)
