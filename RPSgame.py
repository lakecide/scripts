import sys, random

print("ROCK, PAPER, SCISSORS")
#The variables keeps track of user loss, wins and draws
wins = 0
losses = 0
ties = 0

while True: #The main game loop
    
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True: #The player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input().lower()
        if player_move == "q":
            sys.exit()
        if player_move == "r" or player_move == "p" or player_move == "s":
            break #break out of the player loop
        else:
            print("Type one of r, p, s, or q")
    #player input ends here
    
    #player evaluation begins
    if player_move == "r":
        print("ROCK versus ...")
    elif player_move == "p":
        print("PAPER versus ...")
    else:
        print("SCISSORS versus ...")
    
    #computer random selection begins
    computer_count = random.randint(1, 4)
    if computer_count == 1:
        computer_move = "r"
        print("ROCK")
    elif computer_count == 2:
        computer_move = "P"
        print("PAPER")
    else:
        computer_move = "s"
        print("SCISSORS")
    
    # Display / concatenate and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
    #concatenation ends here

#the game loops back from here

