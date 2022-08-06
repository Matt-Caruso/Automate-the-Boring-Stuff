#This project takes a list as a paramter to a function and prints out every item with commas 
global result

def comma(states):
    for x in states:
        result += states.index(x),
    return result




states = []
while True:
    print('Enter the name of a state ' + str(len(states))
          + 'Enter nothing to stop.: ')
    name = input()
    if(name == ''):
        break
states = states + [name]

comma(states)
print(result)
