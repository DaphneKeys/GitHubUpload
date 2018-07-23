#automate the boring stuff with python (page 102)
#using join()
spam=['apple', 'banana', 'tofu','cats']

spam[-1] = 'and ' + spam[-1]
spam = ', '.join(spam)
print(spam)