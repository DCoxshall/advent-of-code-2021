inputFile = open("day1_input.txt", "r")
numbers = [int(i) for i in inputFile.readlines()]
inputFile.close()

# Part 1
total = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        total += 1

print("Part 1: " + str(total))

# Part 2
total = 0
threesum_numbers = []
for i in range(0, len(numbers) - 2):
    threesum_numbers.append(numbers[i] + numbers[i+1] + numbers[i+2])

for i in range(1, len(threesum_numbers)):
    if threesum_numbers[i] > threesum_numbers[i - 1]:
        total += 1

print("Part 2: " + str(total))
input()
