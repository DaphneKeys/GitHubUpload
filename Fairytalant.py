#This program will prompt user to enter a fairy name; blank to quit the system
#if fairy name entered is not in the list, name and talant entered will append the list (list updated)


talant = {'Tinkerbell' : 'Tinker' , 'Rosetta' : 'Gardening'}

while True:
    print('Enter a fairy name: (blank to quit)')
    name = input()
    if name == '':
        print('System break')
        break

    if name in talant:
        print(name+ ' is a '+talant[name]+ ' fairy')
    else:
        print('New fairy '+name+', what talant? :')
        newtalant = input()
        talant[name] = newtalant
        print('New fairy born!')

#Output :-
# Enter a fairy name: (blank to quit)
# Tinkerbell
# Tinkerbell is a Tinker fairy
# Enter a fairy name: (blank to quit)
# Iridessa
# New fairy Iridessa, what talant? :
# Light
# New fairy born!
# Enter a fairy name: (blank to quit)
# Iridessa
# Iridessa is a Light fairy
# Enter a fairy name: (blank to quit)
#
# System break