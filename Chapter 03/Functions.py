# A function is like a mini-program within a program.
from __phello__.ham import eggs


# Example 1

def hello(): #A def statement, which defines a function named hello()

    print('Howdy!')
    print('Howdy!!!')       #Body of function
    print('Hello there.')   #This code is executed when the function is called,
                            # not when the function is first defined.

hello()
hello() # function calls.
hello()

#When the program execution reaches these calls, it will jump to the top
# line in the function and begin executing the code there.

#Since this program call hello() three times, the code in the hello() function is executed
# three times.
print('\n')
# Example 2

#def Statements with Parameters
def hi(name):
    print('Hi ' + name)
hi('Peter')
hi('Carlos')

#The output looks like this:
#   Hi Peter
#   Hi Carlos


print('\n')

# Example 3

# Return values and return Statements
#In general, the value that a function call evaluates to is called the return value of the function.

# A Return Statement consist of the following:
    # The return keyword
    # The value or expression that the function should return


# When an expression is used with a return statement, the return value is what this expression evaluates to. For example,
# the following program defines a function that returns a different string depending on what number ii is passed as an argument.

import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'

r = random.randint(1,9) # It valuates to a random integer between 1 and 9 ( including 1 and 9 themselves),
                              # and this value is stored in a variable named r.

fortune = get_answer(r)        # The getAnswer() function is called with r as the argument. The program execution moves
                              # to the top of the getAnswer() function, and the value r is stored in a parameter
                              #named answerNumber. More details in page 64 of AutomateTheBoringStuffWithPython.
print(fortune)

print('\n')

# Example 4

#You can pass return values as an argument to another function call,
# you could shorten these three lines:
p = random.randint(1,9)
fortune = get_answer(p)
print(fortune)


print('\n')

# Example 5

# The None Value, which represents the absence of a value.
# None is the only value of the NoneType data type.

spam = print('Hello!')
print( None == spam )

# Behind the scenes, Python adds return None to the end of any function definition with no return statement.
# This is similar to how a while or for loop implicity ends with a continue statement. Also, if you use a return
# statement without a value ( that is, just the return keyword by itself), then None is returned.




print('\n')
# Example 6

#The print() function has the optional parameters end and sep to specify what
#should be prunted at the end of its arguments and between its arguments(separating them), respectively.

print('Hello')
print('World')

# However you can set the end keyword argument to change this to a different string.
# For example:
print('Hello', end='')
print('World')

print('\n')

# Example 7

#When you pass multiple strings values to print(), the function will
#automatically separate them with a single space.

print('cats','dogs','mice')

#But you could replace the default separating string by passing the sep
#keyword argument.
print('cats','dogs','mice', sep=',')
print('cats','dogs','mice', sep='--')
print('cats','dogs','mice', sep=' & ')


print('\n')


# Local and Global Scope
# Parameters and variables that are assigned in a called function are said
# to exist in that function's local scope.

# Variables that are assigned outside all functions are said to exist in the global scope.

#A variable that exists in a local scope is called a local variable, while a variable
#that exists in the global scope is called a global variable.

#A variable must be one or the other; it cannot be both local and global.

# There is an important difference between both in the page 67 of  AutomateTheBoringStuffWithPython.

#Example 8

#Local variables cannot be used in the global scope
def spam():
    eggs = 31337
spam()
print(eggs) # The code is trying to find the eggs variable in the Global scope, but it is not defined there.

print('\n')

#Example 9

#Local Scopes cannot use variables in other Local Scopes

#A new local scope is created whenever a function is called,
#including when a function is called from another

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
spam()
 #The upshot is that Local Variables in one function are completely separate from the local variables in another functions.

print('\n')

#Example 10

 #Global Variables can be read from a Local Scope

def spam():
     print(apple)
apple = 42
spam()
print(apple)


print('\n')


#Example 11

#Local and Global Variables with the Same Name

def spam_aux():
    cheese = 'spam local'
    print(cheese)

def ham():
    cheese = 'ham local'
    print(cheese)
    spam_aux()
    print(cheese)

cheese = 'global'
ham()
print(cheese)

# There are three different variables in this program, but confusingly they are all named cheese.
#   a) A variable named cheese that exists in a local scope when spam_aux() is called.
#   b) A variable named cheese that exists in a local scope when ham() is called.
#   c) A variable named cheese that exists in the global scope.

print('\n')

#Example 12

#The Global Statement

#If you need to modify a global variable from within a function, use the global statement.

def pause():
    global rice
    rice = 'red'
rice = 'global'
pause()
print(rice)