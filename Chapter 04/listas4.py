# Methods

# Is the same thing as a function , except it is "called on" a value.

#Finding a Value in a List with the index() Method

spam = ['hello','hi','howdy','heyas']
zero = spam.index('hello') # Position in the list of the word 'hello'
print(zero)

print('\n')

three = spam.index('heyas') # Position in the list of the word 'heyas'
print(three)

print('\n')

# When there are duplicate of the value in the list, the index of its first appearance is returned.

spam = ['Zophie','Pooka','Fat-tail','Pooka']
duplicated_word = spam.index('Pooka')
print(duplicated_word)

print('\n')

# Adding Values to Lists with the append() and insert() Methods

spam = ['cat', 'dog', 'bat', 'moose']
print(spam)

print('\n')

# The insert() method can insert a value at any index in the list.

spam = ['cat','dog','bat']
spam.insert(1,'chicken')
print(spam)

# The append() and insert() methods are list methods and can be called only on list values,
# not on other values such as strings or integers.

print('\n')

#Removing Values from Lists with remove()

spam = ['cat','bat','rat','elephant']
spam.remove('bat')
print(spam)

print('\n')

# If the value appears multiple times in the list, only the first instance of the value will be removed.

spam = ['cat','bat','rat','cat','hat','cat']
spam.remove('cat')
print(spam)

print('\n')

# Sorting the Values in a List with the sort() Method

spam = [2,5,3.14,1,-7]
spam.sort()
print(spam)

print('\n')

spam = ['ants','cats','dogs','badgers','elephants']
spam.sort()
print(spam)

print('\n')

# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.

spam = ['ants','cats','dogs','badgers','elephants']
spam.sort(reverse=True)
print(spam)

print('\n')

# There are three things you should note about the sort() method.
# First, the sort() method sorts the list in place
# Second, you cannot sort list that have both number values and string values in them, since Python doesn't know how to compare these values.
# Third, sort() uses "ASCIIbetical order" rather than actual alphabeticañ order for sorting strings. This means uppercase letters come before lowercase letters.


#If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call.

spam = ['a','z','A','Z']
spam.sort(key=str.lower) #This causes the sort() function to treat all the items in the list as if they were lowercase without actually changing the values in the list.
print(spam)




