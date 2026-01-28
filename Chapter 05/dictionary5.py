# The get() Method

def sep():
    print("\n")
# Fortunately, dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.

picnicItems = {'apples':5, 'cups':2}
print(' I am bringing ' + str(picnicItems.get('cups',0)) + ' cups.')

print('I am bringing ' + str(picnicItems.get('eggs',0)) + ' eggs.')
# Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.


# The setdefault() Method
#       You'll often have to set a value in a dictionary for a certain key only if that key does not already have a value.

spam = {'name': 'Pooka', 'age':5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

sep()

# The setdefault() method offers a way to do this in one line of code

# The setdefault() method is a nice shortcut to ensure that a key exists.

spamAux = {'name':'Pooka','age':5}
spamAux.setdefault('color','black')
print(spamAux)

sep()

spamAux.setdefault('color','white')
# When
# spam.setdefault('color', 'white') is called next, the value for that key is not
# changed to 'white' because spam already has a key named 'color'

print(spamAux)

sep()


# Here is a short program that counts the number of occurrences of each letter in a string

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)

# The program loops over each character in the message variable's string,
# counting how often each character appears

