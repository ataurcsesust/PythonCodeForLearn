class First:
    def __init__(self,val):   #constructor
          self.val=val        # here self is the reference of the current object
    def move(self):
         print('move')

    def draw(self):
        print('draw')


point = First('ataur')
point.x=10      #attribute we can set anywhere of our program
print(point.x)
print(point.val)
point.move()

point2= First('1000')
print(point2.val)
point2.val=297
print(point2.val)
point2.x=20
print(point2.x)
