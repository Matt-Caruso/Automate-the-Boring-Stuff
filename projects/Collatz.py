global num
global v
v = 0
global x
x = 0

def collatz():
    if(x % 2 == 0):
        x = (x / 2)
    else:
        x = (num * x + 1)
    v = x
    print(x)
        
print('Enter a Number')
num = input()
x = num

while(v != 1):
    collatz()


