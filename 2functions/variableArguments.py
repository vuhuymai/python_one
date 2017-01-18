def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)


def myFunc(*args, **kwargs):
    if args:
        for arg in args:
            print(arg)
    if kwargs:
        for key, value in kwargs.items():
            print(key, value)
    if not args and not kwargs:
        print("There is no argument")

# test_var_args('yasoob', 'python', 'eggs', 'test')
myFunc()
myFunc('yasoob')
myFunc(23, temper=2, length=35)
