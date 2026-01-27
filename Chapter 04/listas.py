
animal = ['cat','bat','rat','elephant']

#Negative Indexes
print(animal[-1])

print(animal[-3])

print('The '+ animal[-1]+' is afraid of the ' + animal[-3]+'.')

# Getting Sublists with Slices

print(animal[0:4])

print(animal[1:3])

print(animal[0:-1])

# Leaving out the second index is the same as using the length of the list.
print(animal[:2])

print(animal[1:])

#Leaving out the second index is the same as using the length of the list, which will slice to the end of the list.
print(animal[:])


# Getting a Lists Length with len()
print(f'La longitud de la lista es: {len(animal)}')

#Changing Values in a List with Indexes
animal[1]='chicken'
print(animal)

animal[2]='monkey'
print(animal)

animal[2]=animal[1]
print(animal)

animal[-1]=12345
print(animal)

# List Concatenation and List Replication

new_animal = [1,2,3]+['A','B','C']
print(new_animal)

triplica_lista = ['X','Y','Z']*3
print(triplica_lista)

#Removing Values from Lists with del Statements
numbers = [1,2,3,4,5]
del numbers[2]
print(numbers)
del numbers[2]
print(numbers)


