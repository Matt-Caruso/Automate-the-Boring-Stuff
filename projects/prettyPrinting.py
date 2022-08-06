import pprint

print('Type a message with letters, numbers and characters:')
message = input()

count = {}

for character in message:
    #count.setDefault(character, 0)
    count[character] = count[character] + 1
    
    pprint.pprint(count)