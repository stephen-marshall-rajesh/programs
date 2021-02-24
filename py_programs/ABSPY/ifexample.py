'''
print("What is your name")
name = input()
if name == 'Stephen':
    print('Hi ' + name)
else:
    print('who are you ' + name)
print('Done')

'''

# below program to check password

'''
print ('What is the password')
passwd = str(input())
if passwd == 'ubuntu':
    print('Access Granted')
else:
    print ('Unauthorized Entry')

print('Done')

'''


#yourname program

'''
name = ''
while name != 'stephen':
    print('Please type your name')
    name = input()

print('Thank You ' + name)

'''

#using continue statement

'''
spam = 0

while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

'''

# using for loop

print('My Name is')
for i in range(10):
    print('My Name is steve at index' + str(i))





























