course = "python 'course's for beginners"    #these work only for single line string
course2= 'Hello "world" '  #these work only for single line string


# theree colon is use for multiline  stringg
course2 ='''              
Hi, Asif
I'm here
good bye
'''

print(course)
print(course2)
print(course2)

print(course[0])   #index charecter
print(course[-1])  #print the last charecter of a string
print(course[-2])  # print the second last charecter of a string
print(course[1:3])  #print all charecter from index 1 to 2
print(course[:3])  #print all charecter from index 0 to 2

another = course
print(another)
another = course[:]   # same as, another = course
print(another)


name = 'ataur'
print(name[1:-1])    #print all charecter from index 1 to last except the last charecter