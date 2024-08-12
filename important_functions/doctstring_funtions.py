#We can define the documentation that a function does.

def test_add(a, b): #Si pasas el cursor por encinma de la función, también puedes ver la documentación
    '''
    a: value 1
    b: value 2

    returns: la suma de dos elementos pasados por parámetro

    '''
    return a + b

help(test_add) #Una manera de ver la documentación asociada de la función

'''
Help on function test_add in module __main__:

test_add(a, b)
    a: value 1
    b: value 2

    returns: la suma de dos elementos pasados por parámetro


'''
print(test_add.__doc__) #Otra manera de ver la documentación asociada de la función

'''

    a: value 1
    b: value 2

    returns: la suma de dos elementos pasados por parámetro

'''