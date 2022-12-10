f = open("../input/day5_input.txt")
lines = f.read().splitlines()



#                 [M]     [W] [M]    
#             [L] [Q] [S] [C] [R]    
#             [Q] [F] [F] [T] [N] [S]
#     [N]     [V] [V] [H] [L] [J] [D]
#     [D] [D] [W] [P] [G] [R] [D] [F]
# [T] [T] [M] [G] [G] [Q] [N] [W] [L]
# [Z] [H] [F] [J] [D] [Z] [S] [H] [Q]
# [B] [V] [B] [T] [W] [V] [Z] [Z] [M]
#  1   2   3   4   5   6   7   8   9 


layout = [
    ['B', 'Z', 'T'],
    ['V', 'H', 'T', 'D', 'N'],
    ['B', 'F', 'M', 'D'],
    ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
    ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
    ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
    ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
    ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
    ['M', 'Q', 'L', 'F', 'D', 'S']
]

for line in lines:
    instruction = line.split(' ')
    count, s1, s2 = map(int, [instruction[1], instruction[3], instruction[5]])
    temp = []
    for i in range(count):
        temp.append(layout[s1-1].pop())
    
    temp.reverse()
    layout[s2-1]+=temp
    # n = len(layout[s1-1])
    # stack = layout[s1-1][:n-count-1]
    # layout[s1-1]=stack
    # layout[s2-1]=+stack
    # for i in stack:
    #     print(i)
    # print(layout[s2-1])
    # for i in stack:
    #     layout[s2-1].append(i)
    # print(stack)
    # print(layout[s2-1])
    # for i in range(count):
    #     layout[s2].append(layout[s1].pop()) # Part 1

    

    
        

        


string = ''
print(layout)
for i in layout:
    string+=i.pop()

print(string)