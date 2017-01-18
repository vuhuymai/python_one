# WHY ARE THERE NO ++ AND -- OPERATORS IN PYTHON?
'''
Simple increment and decrement aren't needed as much as in other languages. 
You don't write things like for(int i = 0; i < 10; ++i) in Python very often; 
instead you do things like for i in range(0, 10)
More in the following link:
http://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python
'''

# PYTHON'S NULL EQUIVALENT: None

http://pythoncentral.io/python-null-equivalent-none/

assign the None type to a variable
my_none_variable = None

database_connection = database.connect()
if database_connection is None:
    print('The database could not connect')
else:
    print('The database could connect')
