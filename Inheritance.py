class Mammal:
    def walk(self):
        print('walk')
        
class Dog(Mammal):
    def bark(self):
        print('barking')
    
    def Hi():      # It's a static method
        return (f'Hi,It"s a cat')

class Cat(Mammal):
    pass

print(Dog.Hi())

dog=Dog()
dog.bark()

cat = Cat()
cat.walk()
