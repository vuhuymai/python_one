'''
When we define class A(B): pass, we say A is the child 
of B, and B is the parent of A. parent and base are 
synonyms, as well as child and derived. Also, we say 
that a class inherits from another class, or that 
it extends it.
'''

class Engine():
    def start(self):
        pass

    def stop(self):
        pass

class ElectricEngine(Engine): # Is-A Engine
    pass

class V8Engine(Engine): # Is-A Engine
    pass

class Car():
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()

    def start(self):
        print("Starting engine {0} for car {1}... Wroom, wroom!"
        .format(self.engine.__class__.__name__, self.__class__.__name__))
        self.engine.start()
    
    def stop(self):
        self.engine.stop()

class RaceCar(Car):
    engine_cls = V8Engine

class CityCar(Car):
    engine_cls = ElectricEngine

class F1Car(RaceCar):
    engine_cls = V8Engine

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for eachCar in cars:
    eachCar.start()

""" Prints:
Starting engine Engine for car Car... Wroom, wroom!
Starting engine V8Engine for car RaceCar... Wroom, wroom!
Starting engine ElectricEngine for car CityCar... Wroom, wroom!
Starting engine V8Engine for car F1Car... Wroom, wroom!
"""

print("\nChecking the is-a relationship")
cars = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
car_classes = [Car, RaceCar, F1Car]
for eachCar, car_name in cars:
    for class_ in car_classes:
        belongs = isinstance(eachCar, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)

""" Prints:
car is a Car
car is not a RaceCar
car is not a F1Car
racecar is a Car
racecar is a RaceCar
racecar is not a F1Car
f1car is a Car
f1car is a RaceCar
f1car is a F1Car
"""

print("\nChecking inheritance")
for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1, class2)
        msg = '{0} a subclass of'.format('is' if is_subclass else 'is not')
        print(class1.__name__, msg, class2.__name__)
'''
Car is a subclass of Car ==> a class is a subclass of itself
Car is not a subclass of RaceCar
Car is not a subclass of F1Car
RaceCar is a subclass of Car
RaceCar is a subclass of RaceCar
RaceCar is not a subclass of F1Car
F1Car is a subclass of Car
F1Car is a subclass of RaceCar
F1Car is a subclass of F1Car
'''
