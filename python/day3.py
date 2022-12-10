f = open("../input/day1_input.txt")

lines = f.read().splitlines()

length = len(lines)

low_dict = {}
cap_dict = {}

for i in range(0, 26):
    cap_char = chr(65+i)
    low_char = chr(97+i)
    low_dict[low_char] = i+1
    cap_dict[cap_char] = i+27

score=0

#part 2

for i in range(0, length, 3):
    first = list(lines[i])
    second = list(lines[i+1])
    third = list(lines[i+2])

    first.sort()
    second.sort()
    third.sort()

    i,j=0,0
    a_val = ord('a')
    A_val = ord('A')

    a,b,c,d = 0,0,0,0
    common = []
    while(a<len(first) and b<len(second)):
        # print(common)
        if first[a]==second[b]:
            common.append(first[a])
            a+=1
            b+=1
        elif first[a]<second[b]:
            a+=1
        else:
            b+=1

    common.sort()

    while(third[c]!=common[d]):
        if third[c]<common[d]:
            c+=1
        else:
            d+=1

    sticker = common[d]
    print(common)
    if ord(sticker) > 97 and ord(sticker)< 123:
        score+=low_dict[sticker]
    else:
        score+=cap_dict[sticker]

    

# part 1

# print(cap_dict)

# for line in lines:
#     n = len(line)
#     mid = n//2
#     first = list(line[:mid])
#     second = list(line[mid:])
    
#     first.sort()
#     second.sort()
#     i,j=0,0
#     a_val = ord('a')
#     A_val = ord('A')
    
#     while(first[i]!=second[j]):
#         if first[i]<second[j]:
#             i+=1
#         else:
#             j+=1

#     common = first[i]
#     print(common)
#     if ord(common) > 97 and ord(common)< 123:
#         score+=low_dict[common]
#     else:
#         score+=cap_dict[common]

print(score)


# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg

