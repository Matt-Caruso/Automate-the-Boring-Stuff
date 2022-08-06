#Intermediate List topics

spam = ['cat','rat','dog','bat','fish']
print('The original list is: ', spam)

#Negative indexes
print('The last index is: ', spam[-1]) 
print('The second to last index is: ', spam[-2]) 

#Sublists with splices
print('This is a splice of the list: ', spam[0:2]) 

#In and Not operators
print('howdy' in spam)
print('howdy' not in spam)

#Index()
print(spam.index('bat'))

#Append vs Insert
spam.append('bird')
print('Bird appended to list:', spam)

spam.remove('bird')

spam.insert(2,'bird')
print('Bird Inserted into list:', spam)

#Sort
spam.sort()
print('The sorted list is:', spam)


