text = "Olalekan is not a bad person"
print(text.split())

items = ['he', 'does', 'she']
print(" man ".join(items))
name = "OLA"
print(name.isupper())

subt = '{} will like to meet you {name2}'.format(name, name2='Nafisat')
print(subt)

from string import Template
greeting = Template("$title is not your mate")
greet = greeting.substitute(title='Jumoke')
print(greet)

container = {'key-1': 'lekan', 'key-2': 'Nafisat'}
print(container)
#container['key-3'] = 'Ajani'
if 'key-4' in container:
    print("Key 4 is present")
else:
    container['key-4'] = 'Mustapha'
print(container)
container['key-4']
del(container['key-4'])
print(container)
    



