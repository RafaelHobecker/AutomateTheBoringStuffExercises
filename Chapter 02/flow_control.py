# Chapter 2 - Page Examples

#1.
# if Statements
name = input('What is your name?')
if name == 'Alice':
    print('Hi Alice\n')

# else Statements
else:
    print('Hello, stranger.\n')

#2.
# elif Staments
aux_name=input('What is your name?')
age=int(input('What is your age?'))
if aux_name == 'Peter':
    print('Hi Peter\n')
elif age < 12:
    print('You are not Peter, kiddo.\n')
elif age > 100:
    print('You are not Peter, grannie.\n')
elif age > 2000:
    print('Unlike you, Peter is not an undead, immortal vampire.\n')

#3.
# while Loop Statements
spam = 0
if spam < 5: # just print one time, because is an if, if it is true, it execute the print and break.
    print('Hello World')
    spam = spam + 1
#4.
"""Here's the code with a while statement"""
spam =0
while spam < 5:
    print('Hello World')
    spam = spam + 1

# An Annoying while Loop
#Here is a small example program that will keep asking you to type, literally your name.
#5.
name = ''
while name != 'your name': # If you never enter your name, then the while loop's condition will never be False.
    print('\nPlease type your name.')
    name = input()
print('Thank you for your time!')

# Break Statements
#6.
while True: # This line creates an infinite loop
    print(('\nPlease type your name.'))
    name= input()
    if name == 'your name':
        break
print('Thank you for your time!')


#continue Statements
#7.
while True:
    print('\nWho are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password?(It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Acces granted.')


# 'Truthy' and 'Falsey' Values
#8.
name = ''
while not name: # If the user enters a blank string for name, then the while statement's condition will be True.
    print('\nEnter your name:')
    name = input()
print('How many guest will you have?')
numOfGuest = int(input())
if numOfGuest: #If the value for numOfGuests is not 0, then the condition is considered to be True.
    print('Be sure to have enough room for all your guests.')
print('Done')

