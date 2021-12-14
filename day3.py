#get list of binary numbers as strings
input_file = open("day3_input.txt", "r")
numbers = input_file.readlines()
input_file.close()
for i in range(len(numbers)):
    if numbers[i][-1] == "\n":
        numbers[i] = numbers[i][:-1]

def get_gamma_rate(numbers):
    gamma_rate = ""
    for i in range(len(numbers[0])):
        total = sum([int(j[i]) for j in numbers])
        if round(total / len(numbers), 0) == 1:
            gamma_rate += "1"
        else:
            gamma_rate += "0"
    return gamma_rate

def flip_bits(bin_num):
    new_num = ""
    for i in bin_num:
        if i == "1":
            new_num += "0"
        elif i == "0":
            new_num += "1"
    return new_num

#Part 1
gamma_rate = get_gamma_rate(numbers)
epsilon_rate = flip_bits(gamma_rate)
print("Part 1: " + str(int("0b" + gamma_rate, 2) * int("0b" + epsilon_rate, 2)))

#Part 2
def get_oxygen_rating(numbers):
    bit_pntr = 0
    while(len(numbers)) > 1:
        column = ""
        count1 = 0
        count0 = 0
        for i in [j[bit_pntr] for j in numbers]:
            if i == "1":
                count1 += 1
            else:
                count0 += 1
        if count1 >= count0:
            most_common = "1"
        else:
            most_common = "0"

        numbers = [i for i in numbers if i[bit_pntr] == most_common]
        
        bit_pntr += 1
    return int("0b" + numbers[0], 2)

def get_co2_rating(numbers):
    bit_pntr = 0
    while (len(numbers)) > 1:
        column = ""
        count1 = 0
        count0 = 0
        for i in [j[bit_pntr] for j in numbers]:
            if i == "1":
                count1 += 1
            else:
                count0 += 1
        if count1 < count0:
            least_common = "1"
        else:
            least_common = "0"

        numbers = [i for i in numbers if i[bit_pntr] == least_common]
        
        bit_pntr += 1
    return int("0b" + numbers[0], 2)

o2 = get_oxygen_rating(numbers)
co2 = get_co2_rating(numbers)

print("Part 2: " + str(o2 * co2))
