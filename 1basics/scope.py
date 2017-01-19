'''
Python does not have blocks, as do some other languages
(such as C/C++ or Java)
The scoping unit of python: module, function body, class definition
'''

# For loop is an example
count = 0
for count in range(10):
    print(count, end=' ')
print("\n" + str(count)) //output 9 not 0

    