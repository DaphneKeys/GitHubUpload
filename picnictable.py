#automate the boring stuff with python page 133-134

teaparty = {'sandwiches' : 5, 'Jasmine tea' : 6 , 'Cakes' : 6}

def wonderland(alice,leftwidth,rightwidth):
    print('Tea Party'.center(leftwidth+rightwidth, '-'))
    for k,v in alice.items():
        print(k.ljust(leftwidth,'@') + str(v).rjust(rightwidth))

print('You are invited to our Tea Party')
wonderland(teaparty, 12 , 5)