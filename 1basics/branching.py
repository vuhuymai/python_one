# Ternary operator
'''
added in version 2.5
Syntax: foo = "ValueIfTrue" if test else "ValueIfFalse"
If test evaluates to True then "ValueIfTrue" is returned, else "ValueIfFalse" is returned

Example1:
for car, car_name in cars:
    for class_ in car_classes:
        belongs = isinstance(car, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)

Example2: using the ternary operator inside a string.format() method
for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1, class2)
        msg = '{0} a subclass of'.format(
            'is' if is_subclass else 'is not')
        print(class1.__name__, msg, class2.__name__)

'''

