#Automate the boring stuff with python page 133 and 134
#similar example for picnictable.py

teaparty = {'cakes' : 5, 'Tea' : 10 , 'Sweets' : 5}

def displaylist(prepare,leftwidth,rightwidth):
    print('Things to prepare: '.center(leftwidth+rightwidth,'#'))
    for k,v in prepare.items():
        print(k.ljust(leftwidth, '*') + str(v).rjust(rightwidth))

displaylist(teaparty,20,9)

