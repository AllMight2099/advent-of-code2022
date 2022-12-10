
f = open("../input/day1_input.txt")

lines = f.read().splitlines()

max_val = 0
sum_upto=0
sum_array = []

for line in lines:
    if line == "":
        sum_array.append(sum_upto)
        max_val = max(max_val, sum_upto)
        sum_upto=0
    else:
        sum_upto+=int(line)

sum_array.sort(reverse=True)
max_3 = sum(sum_array[0:3])
print(max_3)