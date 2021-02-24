'''
def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print("Division of number of zero Error")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(21))
'''

print('How many cats do you have')
numcats = input()
try:
    if int(numcats) >= 4:
        print('Thats a lot of cats')
    else:
        print('That not too many of them')
except ValueError:
    print('You did not enter a number')
