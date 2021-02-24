'''
def hello():
    print('Hello')
    print('Hello 1')
    print('Hello 2')

hello()
hello()
hello()
'''


def hello(name):
    print('Hello ' + str(name))

print('What is your name')
name1 = input()
hello(name1)
print('What is the second name')
name2 = input()
hello(name2)
