input_file = open("day6_input.txt", "r")
line = input_file.readline()
LINE = [int(x) for x in line.split(",")]


def single_pass(shoal):
    # This function works as a solution for both parts
    new_dict = {x: 0 for x in shoal}
    for x in shoal:
        if x == 0:
            new_dict[8] = shoal[x]
            new_dict[6] += shoal[0]
        else:
            new_dict[x - 1] += shoal[x]
    return new_dict


shoal = {i: 0 for i in range(8)}
for x in LINE:
    if x in shoal:
        shoal[x] += 1
    else:
        shoal[x] = 1
print(shoal)
for _ in range(256):
    shoal = single_pass(shoal)
print(shoal)
total = 0
for i in shoal:
    total += shoal[i]
print(total)
