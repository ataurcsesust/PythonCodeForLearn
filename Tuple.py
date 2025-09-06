t1 = (1, 2, 3)
t2 = (10,)        # single element tuple needs a comma
t3 = tuple([4,5,6])  # convert list to tuple
print(t1, t2, t3)


t = (10, 20, 30, 40)
print(t[0])     # 10
print(t[-1])    # 40
print(t[1:3])   # (20, 30)  slicing


t = (1, 2, 3)
for item in t:
    print(item)


a = (1, 2)
b = (3, 4)
print(a + b)       # concatenation -> (1, 2, 3, 4)
print(a * 3)       # repetition -> (1, 2, 1, 2, 1, 2)
print(len(a))      # length -> 2
print(2 in a)      # membership -> True


t = (1, 2, 2, 3, 2)
print(t.count(2))   # 3 -> counts how many times 2 appears
print(t.index(3))   # 3 -> index of first occurrence of 3


t = (1, (2, 3), 4)
print(t[1])     # (2, 3)
print(t[1][0])  # 2


lst = [1, 2, 3]
t = tuple(lst)   # list → tuple
lst2 = list(t)   # tuple → list


t = (10, 20, 30)
print(max(t))    # 30
print(min(t))    # 10
print(sum(t))    # 60


t = (1, 2, 3, 4, 5)
print(t[1:4])   # (2, 3, 4)
print(t[::-1])  # (5, 4, 3, 2, 1)  -> reversed tuple
# t[0] = 10   ❌ Error, tuples cannot be changed

#Tuple unpacking
t = (10, 20, 30)
x, y, z = t
print(x, y, z)  # 10 20 30


#If you want to "change" a tuple, convert it to a list first, modify, and then convert back:
t = (1, 2, 3)
lst = list(t)
lst[0] = 10
t = tuple(lst)
print(t)  # (10, 2, 3)
