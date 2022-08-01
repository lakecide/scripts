import string
import math
from array import array


"""
data = ['black', 'blue', 'brown', 'black', 'white', 'black']

for items in data:
    if items == 'black':
        print(f'I only like {items} belts')
    else:
        print(f"I can manage {items} too")

name = "Ajani one"

print(name.isnumeric())
print(name.title())

unsort = "-".join(data)
print(unsort)

listing = unsort.split('-')
listing.append(name)
listing.sort()
print(len(listing))

print(unsort[2:20:3])
listing.insert(1, 'Jumoke')
listing.remove('blue')
listing.remove('brown')
listing.insert(2, 'Nafisat')
listing.pop()
print(listing)

'''
words = ['me', 1, 3, 4]
for values in words:
    name += str(values)
print(name);
'''

print(name.replace('one', 'Jumoke'))

"""
stateandcapital = {
    "lagos" : "Ikeja", "Kwara" : "Ilorin", "Niger" : "Minna", "Taraba": "Jalingo"
}

"""
for states, capital in stateandcapital.items():
    print(f"The capital of {states} is {capital}")

for capital in stateandcapital.values():
    print(capital) if "Minna" in capital else print("Nothing")

    
    #if "Minna" in capital:
     #   print(capital)
    
#print(stateandcapital.keys())

guards = "full, half, open"
guard_list = [f" {guard}-guard" for guard in guards.split(",")]
print(guard_list)

guard_lists=[]
for guard in guards.split(","):
    guard_lists.append(f"{guard}-guard")
    

print(guard_lists
      )
  
  """
  

#MOSH PYTHON ONLINE COURSE FROM SITE NOT YOUTUBE
"""
for x in range(5):
    for y in range(3):
        if x == 1 and y == 1:
            print(x, y)
            break
    #print(x) """
"""
digs = ""   
for char in "python":
    digs += char
print(digs)

numbs = 0
for num in range(1 , 10):
    if (num % 2) == 0:
        numbs += 1
        print(num)
        
print(f"We have {numbs} even number")
"""

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizz buzz"
    if input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input

print(fizz_buzz(7))
figure = list(range(1, 10, 1))
print(list("AJANI"))
print(len(figure))
print(figure[::-2])

print(figure.count(9))
#list
items = [
    ("Product", 10, 1),
    ("Product2", 9, 2),
    ("Product3", 14, 4)
]
"""price = []
    for item in items:
        price.append(item[1])
    print(price)"""
mapped = list(map(lambda item:item[1], items))
[item[1] for item in items]
print(mapped)
#filtered = list(filter(lambda item: item[1] >=10, items))
#filtered = [item[1] >=10 for item in items]
filtered = [item for item in items if item[1] >= 10]
print(filtered)

#words = [details[1] for details in items]
#print(words)
#words = list(map(lambda details: details[1], items))
#print(words)
#list
words = list(details[2] for details in items)
print(words)
for number in items:
    if number[1] >= 10:
        print(number)

num1 = [1, 2, 3]
num2 = [4, 5, 6]

total = list(zip(num1, num2, range(11, 20, 3)))
print(list(total))
for item in total:
    print(item[2])

x = 10
y = 15 
"""
z = 0
z = x
x = y
y = z
print(f"{x} and {y}")
#OR Using turple """
#array
x, y = y, x
print(x , y)
test = array("i", num2)
print(test[2])


stateandcapital["Ogun"] = "Abeokuta"
del(stateandcapital["Taraba"])
print(stateandcapital)
#for state, capital in stateandcapital.items():
  #  print(type(capital))

#dictionaries can also be defined with the dict() function too quick example below
yum = dict(j=2, y=3)
print(yum)
digs = { x : x * 2 for x in range(5)}
print(digs)

#generators which uses ()
digs = (x * 2 for x in range(5))
for gen in digs:
    print(gen)

#unpacking, you can unpack a list with one * and unpack a dictionary with **
#if the key in a dict is equal to another, the last key is used
first = {"a": 2}
second = {"a": 4, "c": 5}
total = {**first, **second}
print(total)


