for i in range(5):
    print(i)


for i in range(5):
    print(i,end=" ")    # to print value without newline we should add, end 


# Range with start and end
for i in range(2, 6):
    print(i)


#range with step
for i in range(0, 10, 2):
    print(i)


for i in range(5, 0, -1):
    print(i)

#Looping through a list

list = ["apple",'banana','lebu']
for item in list:
    print(item,end=" ")

print()

#Looping in a string
str ='My name is Ataur'
for ch in str:
    print(ch,end="")


nums = (10, 20, 30,80,78)
for n in nums:
    print(n)


#List → mutable (you can change, add, remove elements).
#Tuple → immutable (once created, it cannot be changed).