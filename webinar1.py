import find
users = [
    {'first_name': 'Jack 1', 'last_name': 'Black 1', 'age': 90},
    {'first_name': 'Jack 2', 'last_name': 'Black 2', 'age': 199},
    {'first_name': 'Jack 3', 'last_name': 'Black 3', 'age': 21},
    {'first_name': 'Jack 4', 'last_name': 'Black 4', 'age': 32},
    {'first_name': 'Jack 5', 'last_name': 'Black 5', 'age': 45},
    {'first_name': 'Jack 6', 'last_name': 'Black 6', 'age': 23},
    {'first_name': 'Jack 7', 'last_name': 'Black 7', 'age': 2},
    {'first_name': 'Jack 8', 'last_name': 'Black 8', 'age': 65},
    {'first_name': 'Jack 9', 'last_name': 'Black 9', 'age': 12},

]

# ages = [90, 199, 21, 32, 45, 23, 2, 65, 12]

min_num = find.find_min(users)
print(min_num)
