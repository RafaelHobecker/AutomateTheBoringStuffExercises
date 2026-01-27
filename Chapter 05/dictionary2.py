# Dictionaries can still use integers values as keys, just like lists use integers for indexes, but they do not have to start at 0 and can be any number.

spam = {12345: 'Luggage Combination',42: 'The Answer'}
print(spam[12345])

print(spam[42])


# Dictionaries vs Lists

#   While the order of items matters for determining whether two lists are the same, it does not matter in what order the
#   key-value pairs are typed in a dictionary.

#   Lists example
spam = ['cats','dogs','moose']
bacon = ['dogs','cats','moose']
print( spam == bacon) #Return false

#   Dictionaries example
eggs = {'name':'Zophie', 'species':'cat','age':'8'}
ham = {'species':'cat', 'age':'8', 'name': 'Zophie'}
print( eggs == ham) #Return True

# Because dictionaries are not ordered, they can't be sliced like lists.

