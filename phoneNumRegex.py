#Automate the boring stuff with python
#Chapter 7 Regular expression = matching object
import re
message = 'Call me 415-555-1011 tomorrow, or at 415-555-0000'

#search() returns Match Objects - only the first occurence.
phoneNumRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))') #re.compile is looking for the patern of text
mo = phoneNumRegex.search(message) #search the string for the pattern
print(mo.group()) #returns the entire patern

#findall() returns a list of strings - all.
moo = phoneNumRegex.findall(message)
print(moo)