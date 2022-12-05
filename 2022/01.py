from pathlib import Path

file = open("{}\\2022\\01_input.txt".format(Path.cwd()), "r").readlines()
array = [line.replace('\n', '') for line in file]

sum_calories = 0
total_cal_per_elf = []
for value in array:
    if value != '':
        sum_calories = sum_calories + int(value)
    else:
        total_cal_per_elf.append(sum_calories)
        sum_calories = 0

total_cal_per_elf.sort(reverse=True)

sum_of_top_three = 0
for i in range(0,3):
    sum_of_top_three = sum_of_top_three + total_cal_per_elf[i]

print("# Top 5: {}".format(total_cal_per_elf[0:5]))
print("# First answer: {}".format(total_cal_per_elf[0]))
print("# Second answer: {}".format(sum_of_top_three))