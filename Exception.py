try:
    age = int(input('Enter age: '))
    value=2000
    temp= value/age
    print(temp)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be zero')