f = open("../input/day6_input.txt")

line = f.read()
n = len(line)
# for i,j in line:
flag=False
i,j = 0,0
count=0
ind = 0
# print(line[i])

temp = []

while(not flag):
    count=len(temp)
    # temp.append(line[i])
    if count==14:
        flag=True
        break
    elif count<14:
        if line[j] not in temp:
            temp.append(line[j])
            j=j+1
        else:
            # print('here')
            i=i+1
            j=i
            temp=[]
            # count=0       
    else:
        print("something's wrong here")

print(j)


