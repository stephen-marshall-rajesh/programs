# Program to add 0 + 1 + 2 + . . .  + 100

print('Program to print sum of sum of digits supplied by user')

total = 0

print ('Enter the sum  of how many digits you need')
sumdig = int(input())
for num in range(sumdig + 1):
    total = total + num
print(total)
