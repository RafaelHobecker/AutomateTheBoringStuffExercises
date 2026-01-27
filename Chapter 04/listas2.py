# Using for Loops with Lists

for i in range(4):
    print(i)

# The return value from range(4) is a list-like value that Python considers
#similar to [0,1,2,3].

print("\n")
# A common Python technique is to use range(len(someList)) with a for loop to iterative over the indexes of a list.
supplies = ['pens','staplers','flame-throwers','brinders']

for i in range(len(supplies)):
    print('Index '+ str(i) + ' in supplies is: '+supplies[i])


print("\n")

#The __ in __ and __ not __ in Operators

myPets = ['Zophie','Pooka','Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

print("\n")

#The Multiple Assignment Trick

cat = ['fat','black','loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size)
print(color)
print(disposition)

print("\n")

# You could type this line of code

size,color,disposition = cat
print(size)
print(color)
print(disposition)

