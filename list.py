
import random

"""
catNames = []
while True:
    print(f'Enter the name of cat ' + str(len(catNames) +1) + 
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames += [name] #list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
    
"""

#Another Example
supplies = ['pens', 'staplers', 'flamethrowers', 'binders', 'condoms']
#for index in range(len(supplies)):
#    print(f'The index of  {index} is ' + supplies[index])
#print(supplies[0])


#Using the enumerate() Function with Lists
#Instead of using the range(len(someList)) technique     

for item, data in enumerate(supplies):
    print("the index of " + str(item) + ' is ' + data)
  


#Another example
"""
print('Enter the supply you want')
user_input = input()
if user_input in supplies:
    print("We already have that supply challe")
else:
    supplies.append(user_input)
    print(supplies)
    """
    


#print(random.choice(supplies))
#rand = random.choices(supplies)
#print(rand)

#random shuffle example
print(supplies)


itemize = ['latte', 'coffe', 'extra', 'munchit']
supplies += itemize
#append and insert difference

itemize.append('mouse')
print(itemize)
itemize.insert(4, 'ijekuje')
random.shuffle(itemize)
print(itemize)


#scatter = random.shuffle(supplies)
#print(supplies)
#random.shuffle(supplies)
#print(supplies)

#If the value appears multiple times in the list, only the first instance of
#the value will be removed.

check = itemize.index('latte')
print(check)

itemize.insert(5,'toronto')
print(itemize)
itemize.remove('latte')

itemize.sort(reverse = True)

for indexes, datas in enumerate(itemize):
    print((indexes, datas))

print(itemize)

name = 'Ajani'
for i in name:
    
    if i == 'a':
        print(f'** {i} **')
    else:
        print(f'**** {i} ****')

