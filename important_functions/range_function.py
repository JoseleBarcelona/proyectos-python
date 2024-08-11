rgn = range(10)
print(list(rgn))
print(tuple(rgn))
print(set(rgn))

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

'''

rgn2 = range(5, 10)
print(list(rgn2))

#[5, 6, 7, 8, 9]

rgn3 = range(5, 50, 10)
print(list(rgn3))

#[5, 15, 25, 35, 45]

rgn4 = range(100, -110, -10)
print(list(rgn4))

#[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]