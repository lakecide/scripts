import sys, random

"""
while True:
    print("Type exit to Exit the program: ")
    command = input().lower()
    if command == "exit":
        sys.exit()
    print(f"You typed {command}")
    """
    
secre_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

for guess in range(1,7):
    print("Take a guess")
    guessed_number = int(input("What is your guess: " ))
    if guessed_number < secre_number:
        print("Your guess is too low")
    elif guessed_number > secre_number:
        print("Your guess is too high")
    else:
        break
if guessed_number == secre_number:
    print(f"Good job, you guessed my number in {guess} guesses")
else:
    print(f"The number i was thinking of is {secre_number}")
