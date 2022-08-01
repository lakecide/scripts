import random, time, sys

"""
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return "This is number 2"
    elif answerNumber == 3:
        return "Yes, this is the third"
    elif answerNumber == 4:
        return "Reply with the number 4"
    else:
        
        return "This is the end of the ROAD 5"


number = random.randint(1, 5 + 1)

print(getAnswer(random.randint(1, 6)))
"""
#print(getAnswer(number))

#print("testing", )


def spam():
    print(eggs)
eggs = 42
spam()
#print(eggs)

#this is the beginning of the zigzag test game

indent = 0 #how many spaces to indent
indentIncreasing = True  #whether the indentation is increasing or not

try:
    while True: #the main program
        print(' ' * indent, end='')
        print('********')
        time.sleep(2) #pauses the game for less than a sec
        
        if indentIncreasing:
            #Increase the number of spaces
            indent += 1
            if indent == 20:
                #change direction
                indentIncreasing = False
        else:
            #Decrease the number of spaces
            indent -= 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt():
    sys.exit()


