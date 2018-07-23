passerby = []

while True:
    print('Enter names that have came to Wonderland:')
    names = input()
    if names == 'Alice':
        print('Alice was here?')
        print('THE Alice? When did she come?')
    elif names == '':
        break
    passerby = passerby + [names]


print('List of all passerby:')
for names in passerby:

    print(' ' +names)

