input_file = open("day2_input.txt", "r")
commands = input_file.readlines()
input_file.close()


# Part 1
for i in range(len(commands)):
    if commands[-1] == "\n": # remove the newline character for simplicity
        commands[i] = commands[i][:-1] 

x = 0
y = 0

for i in commands:
    fields = i.split(" ")
    distance = int(fields[-1])
    direction = fields[0]

    if direction == "forward":
        x += distance
    if direction == "up":
        y -= distance
    if direction == "down":
        y += distance

print(x * y)

# Part 2

x = 0
y = 0
aim = 0

for i in commands:
    fields = i.split(" ")
    distance = int(fields[-1])
    direction = fields[0]

    if direction == "up":
        aim -= distance
    if direction == "down":
        aim += distance
    if direction == "forward":
        x += distance
        y += aim * distance

print(x * y)
