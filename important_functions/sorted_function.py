#sorted() ordena los elementos de una lista, tupla o conjunto.

numbers = [5, 4, 8, 9, 10, 0, -3, -2, 1]
print(sorted(numbers))
#[-3, -2, 0, 1, 4, 5, 8, 9, 10]

print(sorted(numbers, reverse=True))
#[10, 9, 8, 5, 4, 1, 0, -2, -3]