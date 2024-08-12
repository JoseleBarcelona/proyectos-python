people = [
    {'name': 'John', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 35},
    {'name': 'Charlie', 'age': 20}
]

sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)
#[{'name': 'Charlie', 'age': 20}, {'name': 'Bob', 'age': 25}, {'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 35}]

sorted_people = sorted(people, key=lambda person: person['name'])
print(sorted_people)
#[{'name': 'Alice', 'age': 35}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 20}, {'name': 'John', 'age': 30}]

sorted_people = sorted(people, key=lambda person: person['name'], reverse=True)
print(sorted_people)
#[{'name': 'John', 'age': 30}, {'name': 'Charlie', 'age': 20}, {'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 35}]