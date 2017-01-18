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

