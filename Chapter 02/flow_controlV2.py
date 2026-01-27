# Add up all the numbers from 0 to 100
#1.
total=0
for num in range(101):
    total=total+num
print(total)

# An equivalent while Loop
#2.
print('\nMy name is')
i=0
while i<5:
    print('Jimmy Five Times (' + str(i) + ')')
    i=i+1
print('\n')


# The Starting, Stopping, and Stepping Arguments to range()
#3.
# range(x,y): the first argument(X) will be where the for loop's variable starts
            # the second argument(Y) will be up to, but not including, the number to stop at.

for i in range(12,16):
    print(i)


print('\n')
# 4.
# range(x,y,z): the first 2 arguments will be the star(X) and stop(Y) values, and the 3rd(Z) will be the step argument.
for i in range(0,10,2): #will count from zero to eight by intervals of two.
    print(i)

print('\n')

#5.
#You can even use negative numbers for the step argument to make the for loop count down instead of up

for i in range(5,-1,-1): # should print form five down to zero.
    print(i)
