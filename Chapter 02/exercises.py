# 9. Write code that prints Hello if 1 is stored in spam,
# prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = int(input('Introduzca el estado de spam: '))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

# 12. What is the difference between range(10), range(0,10), and range(0,10,1) in a for loop?
print('First loop for with range(10)')
for i in range(10): #i starts in 0, and ends in 10.
    print(i)

print('Second loop for with range(0,10)') #from i=0 to i=10

for i in range(0,10):
    print(i)

print('Third loop for with range(0,10,1)') #from i=0 to i=10, by step of 1
for i in range(0,10,1):
    print(i)

