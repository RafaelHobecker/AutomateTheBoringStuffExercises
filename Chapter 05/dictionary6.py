import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)

# This is helpful when you want a cleaner display of the items in a dictionary than what print() provides.
# The pprint.pprint() function is especially helpful when the dictionary itself contain nested lists or dictionaries.
