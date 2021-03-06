
'''
supplies = ['pen','books','staplers','pins','pen','books','staplers','pins','pen','books','staplers','pins','pen','books','staplers','pins']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
'''
#program to understand references to list
'''
nums =[1,2,3]
for x in nums:
    x = x* 10
    print(x)
    print(nums[0])
    print(nums)
'''


'''

#MUTATES ARGUMENT
#complex example in functions
#program to add value twice to end of list

def append_twice(a_list,val):
    a_list.append(val)
    a_list.append(val)
    print(nums)
    return
nums = [1,2,3]
append_twice(nums,7)
print(nums)

'''
'''
# Below program is incorrect way of using
#program to add value twice but which destroyed at end of function

def append_twice_bad(a_list,val):
    a_list = a_list + [val,val] 
    print(a_list)
    return

    
nums = [1,2,3]
append_twice_bad(nums,7)
print(nums)
'''
# Program RETURNS NEW List better way of using list and do not mutate the original
def append_twice_good(a_list,val):
    a_list = a_list + [val,val]
    return a_list

nums = [1,2,3]
nums = append_twice_good(nums,7)
print(nums)

# python is dynamically typed names has no types associated can be anything
# Names have no type
# values have no scope

'''
#making a 2D  list
#python gets called by assignment

#good way
board1 = [[0] * 8 for _ in range(8)]
print(board1)

#bad way
board = [[0] * 8] * 8
print(board)

'''







    
    

