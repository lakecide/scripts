"""
is_hot = False
is_cold = False
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm cloths")
else:
    print("It is a lovely Day")



#program to check for credit score
price = 1000000
is_credit_good = False
if is_credit_good:
    payment = price * 0.1
    print(f"You need to pay {payment}")
else:
    payment = price * 0.2
    print("You need to pay ",payment)
print(f"Down payment is ${payment}")


high_income = False
credit_score = True

if high_income or credit_score:
    eligible = True
    if eligible:
        print("You are qualified for a loan")
    else:
        print("Please make more transactions on the platform")
else:
    print("You are not qualified for a loan")

    
temp = int(input("Enter your temperature: "))
fig = input("Enter only first letter F(Ferenheit) or C(Celcius): ")

if temp > 30:
    print("Its a hot day")
    print(f"And your temperature is {temp}{fig.upper()}")
    
    
weig = int(input("Weight: "))
type = input("(L)bs or (K)g: ")
if type.upper() == "L":
    kilo = 0.453 * weig
    print(f"You are {kilo}kg")
elif type.upper() == "K":
    pound = 2.205 * weig
    print(f"You are {pound}pounds")
else:
    print("Your weight cannot be calculated")

i = 1
while i <= 5:
    print('      *' * i)
    i += 1
print("doning")


#A guessing game code
correct_value = 9
guess_init = 0
guess_limit = 3
while guess_init < guess_limit:
    guess = int(input("Guess: "))
    guess_init += 1
    if guess == correct_value:
        print("Yes,  You got it right")
        break
else:
    print("Sorry, You missed it")
    


command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!!")
        else:
            started = True
            print("Car started... Ready to go.")
    elif command == "stop":
        if not started:
            print("Car already stopped bitch")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
#   Start - to start the car
#   Stop - to stop the car
#   quit - to exit
""")           
    elif command == "quit":
        break
    else:
        print("I dont understand")
  


##FOR LOOPS

numbers = [2, 2, 2, 2, 7]
values = [5, 2, 5, 2, 2]

for items in numbers:
    output = ""
    for value in range(items):
        output += "x"
    print(output)
print("")
for a in values:
    out = ""
    for num in range(a):
        out += "x"
    print(out)
     
    """
    
#LISTS
"""
lists = [2, 5, 9, 10, 4, 15, 30, 1]
highest = lists[0]
for items in lists:
    if items > highest:
        highest = items
print(highest)
    """   
    
numbers = [5, 7, 10, 8, 5, 2]
numbers.sort()
digits = []

for items in numbers:
    if items not in digits:
        digits.append(items)
print(digits)
"""
print(" ")
print("%s + %s = %s" % (1, 2, "Three"))
print('{} comes before {}'.format('first', 'second'))

print('{1} comes after {0}, but {1} comes before {2}'.format('first', 'second', 'third'))

print(
'''{country} is an island.
... {country} is off of the coast of
... {continent} in the {ocean}'''.format(ocean='Indian Ocean', continent='Africa', country='Madagascar'))
print(" ")

def greetings(firstname, lastname):
    print(f"Welcome Master {firstname}",  lastname)
    print("Enjoy the rest of your day")
    
firstname = input("Enter your firstname: ").lower()
lastname = input("Enter your last name: ").lower()
print(" ")
greetings(firstname, lastname) """

def calculator(num1, num2):
    total = num1 * num2
    return total

print(calculator(5, 5))

"""
def reaction(message):
    words = message.split(" ")
    emojis = {
        ":)": "@#",
        ":(": "$%"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(reaction(message))
"""

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def details(self):
        print("my " + self.name + " is " + self.color)

apple = Fruit("Ajani", "Blue")
apple.details()



class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"{self.name} is a naughty boy")
        
peep = Person("Ajani")
peep.talk() 
print(peep.name)



commit from git
commit another way
what is cashout
