from ast import Num


def collatz(x):
    if(x % 2 == 0):
        x = (x / 2)
    else:
        x = (num * x + 1)
    v = x
    return(x)
        
print('Enter a Number')
global num
global v 
v = 0
num = input()

while(v != 1):
    print(collatz(num))


