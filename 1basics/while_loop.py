print("\nThe while loop")
print("\nFind the binary representation for number 39: 100111")
n = 39
remainders = []
while n > 0:
    remainder = n % 2  # remainder of division by 2
    remainders.append(remainder)  # we keep track of remainders
    n //= 2  # we divide n by 2
# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)

'''
THE WHILE-ELSE CLAUSE
    - is only executed when your while condition becomes false (i.e. the block exits normally)
    - will not executed if you break out of the loop, or if an exception is raised

One way to think about it is as an if/else construct with respect to the condition:
if condition:
    handle_true()
else:
    handle_false()

is analogous to the looping construct:

while condition:
    handle_true()
else:
    # condition is false now, handle and go on with the rest of the program
    handle_false()

Some pseudocode to consider
while value < threshold:
    if not process_acceptable_value(value):
        # something went wrong, exit the loop; don't pass go, don't collect 200
        break
    value = update(value)
else:
    # value >= threshold; pass go, collect 200
    handle_threshold_reached()
'''
print("\nThe while-else clause")
count = 0
while count < 5:
    print("count = " + count + " is less than 5")
    count + +
else:
    print("count = " + count + " is no longer less than 5")
