#Beginner and Intermediate topics for dictionaries

myCat = {'size': 'fat', 'color': 'grey', 'name': 'Gracie'}
print('Original dictionary is:', myCat)

#Getting values from keys
print('My cat is', myCat['size'])
print('')
#for loop for values/keys/items
print('Printing values:')
for x in myCat.values():
    print(x)
print('')

print('Printing Keys:')
for x in myCat.keys():
    print(x)
print('')

print('Printing items:')
for x in myCat.items():
    print(x)
print('')

#get() method - Has a fallback option
print('Her color is: '+ str(myCat.get('color', 'blue')))
print('Her favorite food is: '+ str(myCat.get('food', 'fish')))