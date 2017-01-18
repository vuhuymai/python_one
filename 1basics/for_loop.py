print("\nSimple for in loop")
for number in [1, 2, 3, 4, 5]:
    print(number, end=' ')
print()

print("\nIterating over a range")
for number in range(5):
    print(number, end=' ')
print()

print("\nThe continue statement")
from datetime import date, timedelta
today = date.today()
tomorrow = today + timedelta(days=1)  # today + 1 day is tomorrow
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8  # equivalent to applying 20% discount
    print('Price for sku', product['sku'], 'is now', product['price'])

print("\nThe break statement")
items = [0, None, 0.0, True, 0, 7]  # True and 7 evaluate to True
found = False  # this is called "flag"
for item in items:
    print('scanning item', item)
    if item:
        found = True  # we update the flag
        break
if found:  # we inspect the flag
    print('At least one item evaluates to True')
else:
    print('All items evaluate to False')

'''
THE FOR-ELSE CLAUSE
    - is only executed when your while condition becomes false (i.e. the block exits normally)
    - will not executed if you break out of the loop, or if an exception is raised
'''
print("\n*The special else clause")
print("\nFirst, understand the flag pattern")
people = [('James', 17), ('Kirk', 9), ('Lars', 16), ('Robert', 8)]
driver = None
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
if driver is None:
    print("Driver not found!!!")
else:
    print("The driver is", driver[0], "with age", driver[1], end=' ')
print("\nNow apply the special else clause")
for person, age in people:
    if age >= 18:
        driver = (person, age)
        print("The driver is", driver[0], "with age", driver[1], end=' ')
        break
else:
    print("Driver not found!!!")
print()
