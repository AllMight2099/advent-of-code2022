f = open("../input/day1_input.txt")

lines = f.read().splitlines()
strategy_guide = []
for line in lines:
    strategy_guide.append(line.split(' '))
# Rock - A, X
# Paper - B, Y
# Scissor - C, Z

# strat = {
#     'A': 'X'
# }
# loses = [['A','Z'], ['B', 'X'], ['C', 'Y']]
# wins = [['A','Y'], ['B', 'Z'], ['C', 'X']]
# draw = [['A','X'], ['B', 'Y'], ['C', 'Z']]

# loses = [['A','Z'], ['B', 'X'], ['C', 'Y']]
# wins = [['A','Y'], ['B', 'Z'], ['C', 'X']]
# draw = [['A','X'], ['B', 'Y'], ['C', 'Z']]

wins = {
    'A' : 2,
    'B' : 3,
    'C' : 1
}

loss = {
    'A' : 3,
    'B' : 1,
    'C' : 2
}

draw = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}


# score_play = {
#     'A':1,
#     'B':2,
#     'C':3
# }

# play = {
#     'A': [1, ''],
#     'B': [2],
#     'C': [3]
# }

score=0

# for round in strategy_guide:
#     round_score = score_play[round[1]]
#     if round in wins:
#         round_score+=6
#     elif round in draw:
#         round_score+=3
#     # print(round_score)
#     score+=round_score

for round in strategy_guide:
    if round[1]=='X':
        score=score+loss[round[0]]
    elif round[1]=='Y':
        score=score+draw[round[0]]+3
    elif round[1]=='Z':
        score=score+wins[round[0]]+6
    
    # score+=round_score
    


print(score)