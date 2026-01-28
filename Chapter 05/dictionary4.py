# The keys(), values(), and items() Methods

def sep():
    print('\n')

# The values returned by these methods are not true lists: They cannot be modified and do not have an appende() method.

spam = {'color':'red','age': 42}

for v in spam.values():
    print(v)

sep()

# Here, a for loop iterates over each of the values in the spam directory.
# A for loop can also iterate over the keys or both keys and values:

for k in spam.keys():
    print(k)
sep()

for i in spam.items():
    print(i)

sep()
# Notice that the values in the dict_items value returned by the items() method are tuples of the key value

aux = {'color':'red','age': 42}
print(aux.keys())
sep()
print(list(aux.keys()))
sep()

# Checking Whether a Key or Value Exists in a Dictionary

spam = {'name': 'Zophie','age':7}
print('name' in spam.keys())

sep()

print('Zophie' in spam.values())

sep()

print('color' in spam.keys())

sep()

print('color' not in spam.keys())

sep()

print('color' in spam)

sep()

