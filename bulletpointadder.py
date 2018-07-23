#This program adds a '*' in front of the copied text
#for example copy the following
# hello hello
# helllo
# fun fun flowers


import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)

#Output:
#
# * hello hello
# * helllo
# * fun fun flowers