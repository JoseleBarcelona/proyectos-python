#La función sum(), suma todos los elementos de una lista, una tupla o un conjunto.

numbers = [5, 6, 7, 8, 9]
print(sum(numbers))
#35

print(sum(numbers, start=10))
#45

print(sum(numbers, start=-10))
#25

numero = range(6)
print(sum(numero))
#15

numero = range(6, 10)
print(sum(numero))
#30

numero = range(6, 10, 2)
print(sum(numero))
#14
