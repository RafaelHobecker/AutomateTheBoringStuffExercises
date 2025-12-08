
spam = ['cat','bat','rat','elephant']

#Negative Indexes
print(spam[-1])

print(spam[-3])

print('The '+ spam[-1]+' is afraid of the ' + spam[-3]+'.')

# Getting Sublists with Slices

print(spam[0:4])

print(spam[1:3])

print(spam[0:-1])

# Leaving out the second index is the same as using the length of the list.
print(spam[:2])

print(spam[1:])

#Leaving out the second index is the same as using the length of the list, which will slice to the end of the list.
print(spam[:])


# Getting a Lists Length with len()
print(f'La longitud de la lista es: {len(spam)}')

#Changing Values in a List with Indexes
spam[1]='chicken'
print(spam)

spam[2]='monkey'
print(spam)

spam[2]=spam[1]
print(spam)

spam[-1]=12345
print(spam)
