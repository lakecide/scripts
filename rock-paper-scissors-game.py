import sys, random

print("ROCK, PAPER, SCISSORS")
#These are the variables to keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True: #The main game loops
    #print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print(f'{wins} Wins, {losses} Losses, {ties} ties')
    while True: #the players input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  #quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of the player input loop.
        print('Type one of r, p, s, or q.')
    #Display what the player choose:
    if playerMove == 'r':
        print('ROCK versus ...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    #Display what the computer choose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")
    #Display and record the win/loss/tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
                