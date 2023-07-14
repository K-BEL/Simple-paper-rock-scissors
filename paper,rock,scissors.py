import random

A = 'rsp'
playerturn = str(input('rock (r) , scissors (s) or paper (p) ?'))
ct = random.choice(A)
print(playerturn, 'vs', ct)
if ct == playerturn :
    print('DRAW')
elif ct == 'r':
    if playerturn == 's':
        print('YOU LOSE')
    else:
        print('YOU WIN')
elif ct == 's':
    if playerturn == 'p':
        print('YOU LOSE')
    else:
        print('YOU WIN')
else :
    if playerturn == 'r':
        print('YOU LOSE')
    else:
        print('YOU WIN')

print('HOPE YOU PLAY AGAIN')









