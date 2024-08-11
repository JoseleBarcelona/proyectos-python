#We can define the documentation that a function does.

def test_add(a, b):
    '''
    a: value 1
    b: value 2

    returns: int

    '''
    return a + b

help(test_add)

'''
Help on function test_add in module __main__:

test_add(a, b)
    a: value 1
    b: value 2

    returns: int

'''