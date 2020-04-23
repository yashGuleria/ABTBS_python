import random , sys
print('ROCK','PAPER','SCISSOR')

#these variables will keep a track of the number of losses,wins, and draws
wins=0
losses=0
ties=0

while True:
    print('%s wins, %s losses, %s draws' %(wins, losses, ties))
    playerMove=input()
    if playerMove=='q':
        sys.exit() # quit the program
    if playerMove=='r' or playerMove=='p' or playerMove=='s':
        break    #break out of the layer input loop!!

#display what player chooses
if playerMove=='r':
    print('ROCK versus....')
elif playerMove=='p':
    print('PAPER versus...')
else:
    print('SCISSORS versus....')

#display what computer chooses
randomNumber = random.randint(1,3)
if randomNumber == 1:
    computerMove='r'
    print('ROCK')
elif randomNumber==2:
    computerMove='p'
    print('PAPER')
else:
    computerMove='s'
    print('SCISSORS')

# display and record win/loss/ties
if playerMove == computerMove:
    print('it a tie!! LOL')
elif playerMove=='r' and computerMove=='s':
    print("you win,YEAH!")
    wins=wins+1
elif playerMove=='p' and computerMove=='r':
    print('you win!')
    wins+=1
elif playerMove=='s' and computerMove=='p':
    print('you win!')
    wins+=1
elif playerMove=='r' and  computerMove=='p':
    print('you lost!')
    losses+=1
elif playerMove=='p' and computerMove=='s':
    print('you lost!')
    losses+=1
elif playerMove=='s' and computerMove=='r':
    print('ypu lost!!')
    losses+=1
    