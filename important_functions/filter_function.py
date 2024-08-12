'''
La función filter cojerá cada elemento en un objeto iterable, le pasará una función que definamos nosotros
y si el resultado es True, retornará la función, si es False, eliminará el valor iterable
que no pase el filtro.

'''

strings = ["my", "world", "apple", "pear"]

def longer_than_four(cadena_de_texto):
    return len(cadena_de_texto) > 4

filtered = filter(longer_than_four, strings)
print(list(filtered))

#['world', 'apple']

filtered2 = filter(lambda x: len(x) > 4, strings) #Esto hace lo mismo que el anterior, sin una función específica.
print(list(filtered2))

#['world', 'apple']