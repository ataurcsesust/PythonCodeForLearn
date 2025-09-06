list = ["apple",'banana',3,6,'lebu']
for item in list:
     print(item)

list.append('jambura')     #add at the end 
list.insert(2, 25)         # add at index 2
list.extend([60, 70])      # add multiple
print(list)


list.remove(3)   # remove first occurrence of value
print(list)
x = list.pop()    # remove last element and return the element
print(x)
y = list.pop(2)   # remove element at index 2  and return the element
print(y)
del list[0]       # delete by index  but do not return the element
print(list)
#lst.clear()      # remove all elements
print(list[0])    # 10   (first element)
print(list[-1])   # 40   (last element)
print(list[1:3])  # [20, 30] (slicing)
list[1] = 99
print(list)


nums = [10, 20, 30, 40, 20]
print(20 in nums)        # True
print(nums.count(20))    # 2 (number of occurrences)
print(nums.index(30))    # 2 (first index of 30)
nums.sort()             # ascending
print(nums)             # [10, 20, 30, 40]
nums.sort(reverse=True) # descending
print(nums)             # [40, 30, 20, 10]
nums.reverse()          # reverse order
print(nums)             # [10, 20, 30, 40]
a = [1, 2, 3]
b = a.copy()        # shallow copy
c = a        # another way
print(b, c)
print('audhfsklhfsd')
print(sum(nums))     # 15
print(max(nums))     # 5
print(min(nums))     # 1
print(len(nums))     # 5



#2D list
matrix =[
     [1,2,3],
     [4,5,6],
     [7,8,9]
]

for row in matrix:
     for i in row:
          print(i,end=" ")
     print()


