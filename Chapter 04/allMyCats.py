catNames = []
while True:
    print('Enter the name of a cat '+str(len(catNames)+1) + '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
print('The cats names are:')
for name in catNames:
    print(' '+name)