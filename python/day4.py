f = open("../input/day4_input.txt")

lines = f.read().splitlines()

count=0

for line in lines:
    pairs = line.split(',')
    # print(pairs)
    # pairs.sort()
    l1, r1 = map(int, pairs[0].split('-'))
    l2, r2 = map(int, pairs[1].split('-'))
    
    # Part1 
    # if l1<=l2 and r1>=r2:
    #     count+=1
    #     # print(line)
    # if l1>=l2 and r1<=r2:
    #     count+=1
    # if l1==l2 and r1==r2:
    #     count-=1

    # Part 2
    if l2<l1 and r2<l1:
        count+=1
    if l2>r1 and r2>r1:
        count+=1
    # if l1>l2 and r1<l2:
    #     count+=1


count = 1000-count
# print(len(lines))
print(count)