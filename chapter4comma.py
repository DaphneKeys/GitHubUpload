#Automate the boring stuff with Python (page 102)

spam = ['apples', 'bananas', 'tofu', 'cats']

def eggs(listvalue):
    for i in range(len(listvalue)):
        print(listvalue[i] + ', ', end="")
        if listvalue[i] == listvalue[-2]:
            print('and ' + listvalue[-1], end="")
            break

eggs(spam)