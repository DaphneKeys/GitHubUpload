#automate the boring stuff with python page 87
#myPets.py included while True, if not my pet, ask pet name again.

myPets = ['Nala', 'Jen','Meow']
while True:
    print('Enter my pet name:')
    petname = input()
    if petname not in myPets:
        print('That is not my pet...')
        continue
    else:
        print('That is indeed my pet, '+petname)