#displays based on list of allguests
#Number of things being brough:
# - Apple      7
# - Apple Pie      1
# - Ham sandwiches      3

allguests = {'Alice' : {'apple' : 5, 'pretzel' : 12},
             'Bob' : {'ham sandwiches' : 3, 'apple' : 2},
             'Carol' : {'cups' : 3 , 'apple pie' : 1}}

def total(guests, stuff):
    itemsbrought = 0
    for k,v in guests.items():
        itemsbrought = itemsbrought + v.get(stuff, 0)
    return itemsbrought

print('Number of things being brough:')
print(' - Apple      ' + str(total(allguests, 'apple')))
print(' - Apple Pie      ' + str(total(allguests, 'apple pie')))
print(' - Ham sandwiches      ' + str(total(allguests, 'ham sandwiches')))
