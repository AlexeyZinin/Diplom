print(type(1))
print(type(1/2))
print(type("1/3"))
print(type("1a"))
print(type('Opa'))
print(type(True))
print(type(False))
print(type(None))

s = '01234567RRTY8qwerty'
a = 'qwertyui'
b = 'ASDFGHJK'
s = s + 'pops'
print(s)
print(s[-1:3:-1])
print(s[3:])
print(s.upper())
print(s.lower())
print(s[8:9].lower())
print(s[6:15].upper())

print(a.islower())
print(b.isupper())

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', [1, 2, 3]]
print(type(numbers))
print(numbers[-1])
print(numbers[:10])
print(numbers[-1][0])
numbers.append(numbers[:2])
print(numbers)


users = [
    {'first_name': 'Jack', 'last_name': 'Black', 'age': 100},
    {'first_name': 'Mary', 'last_name': 'Jane', 'age': 40}
]

# user = {'first_name': 'Jack', 'last_name': 'Black', 'age': 100}
print(users[1]["age"])
users[0]['rate'] = 7.8
print(users[0])