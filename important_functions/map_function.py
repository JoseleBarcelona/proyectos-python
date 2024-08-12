#map function allows to apply a function to every single item in an iterable object.
#an iterable object is anything that you can loop through

strings = ["my", "world", "apple", "pear"]

lengths = map(len, strings) #A la función map le podemos pasar cualquier función (en este caso la función len()) a un objeto iterable (strings)
print(list(lengths)) #Lo convertimos a lista para hacerlo iterable

#[2, 5, 5, 4]

lengths2 = map(lambda x: x + "s", strings) #la función anónima lambda agrega una s al final de los valores iterables
print(list(lengths2))

#['mys', 'worlds', 'apples', 'pears']

def add_symbol(string):
    return string + "/"

lengths3 = map(add_symbol, strings)
print(list(lengths3))

#['my/', 'world/', 'apple/', 'pear/']

