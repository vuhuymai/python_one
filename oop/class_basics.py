
# The most simple class
class Simplest(): # when empty, the braces are optional
    pass

print("\nA class is an object of class 'type'")
print(type(Simplest)) # <class 'type'>

print("\n__main__ is the name of the scope in which top-level code")
simp = Simplest() # we create an instance of Simplest: simp
print(type(simp)) # <class '__main__.Simplest'>

print("\nCheck if an object is an instance of a class")
print(type(simp) == Simplest) # True
# This way is better
print(isinstance(simp, Simplest)) # True

'''
- The class object has been created (which usually happens when 
the module is first imported), it basically represents a namespace
- Each instance inherits the class attributes and methods and 
is given its own namespace.
'''
class Person():
    species = 'Human'

print(Person.species) # Human
Person.alive = True # Added dynamically!
print(Person.alive) # True

man = Person()
print(man.species) # Human (inherited)
print(man.alive) # True (inherited)

Person.alive = False
print(man.alive) # False (inherited)

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname) # Darth Vader

'''Attribute shadowing'''

class Point():
    x = 10
    y = 7

p = Point()
print(p.x) # 10 (from class attribute)
print(p.y) # 7 (from class attribute)

p.x = 12 # p gets its own 'x' attribute
print(p.x) # 12 (now found on the instance)
print(Point.x) # 10 (class attribute still the same)

del p.x # we delete instance attribute
print(p.x) # 10 (now search has to go again to find class attr)

p.z = 3 # let's make it a 3D point
print(p.z) # 3

# print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'

'''
Instance method
self is always the first attribute of an instance method
'''
class Square():
    side = 8
    def area(self): # self is a reference to an instance
        return self.side ** 2

sq = Square()
print(sq.area()) # 64 (side is found on the class)
print(Square.area(sq)) # 64 (equivalent to sq.area())

sq.side = 10
print(sq.area()) # 100 (side is found on the instance)

'''
There are two ways to call an instance method
- use the syntax: instanceOfAClass.instanceMethod()
- another syntax: ClassName.instanceMethod(instanceOfThatClass)
'''

class Price():
    def final_price(self, vat, discount=0):
        return (self.net_price * (100 + vat) / 100) - discount

p1 = Price()
p1.net_price = 100

print(Price.final_price(p1, 20, 10)) # 110 (100 * 1.2 - 10)
print(p1.final_price(20, 10)) # equivalent