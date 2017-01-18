from time import sleep, time
from functools import wraps

# why both of the decorators return result, I don't know
#  This is because one decorator uses the return result of
# the other decorator, so we need to return result in both
# decorator so that  we can use in both cases, @measure first,
# then @max_result  or the other way round

# Test this by comment out return in measure, and execute @measure
# first, there will be an error msg


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper


def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print(
                'Result is too big ({0}). Max allowed is 100.'.format(result))
        return result
    return wrapper

# max_result is executed first, and return the value so
# that measure can use to  execute later


@measure
@max_result
def cube(n):
    return n ** 3

print(cube(2))
print(cube(5))
