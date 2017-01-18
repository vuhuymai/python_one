
print("\nGet the type of objects")
myNum = 5
myString = "hello"
print(type(myNum), type(myString), end='')

print("\nThe range function")
# https://docs.python.org/3.5/library/stdtypes.html#range
myRange = range(10)
print(type(myRange))
print(list(myRange))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3, 8)))  # [3, 4, 5, 6, 7]
print(list(range(-10, 10, 4)))  # [-10, -6, -2, 2, 6]

print("\nThe enumerate function")
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)
'''
0 Rivest
1 Shamir
2 Adleman
'''
# enumerate(iterable, start), and it will start from start, rather than 0

print("\nUsing the zip function")
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
for person, age in zip(people, ages):
    print(person, age)

print("\nUsing the zip function with multiple sequences")
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

print("\nExplode the tuple within the body of the for loop")
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)
