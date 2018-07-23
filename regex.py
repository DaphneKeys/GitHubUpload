#!python3
#Automate the boring stuff with python - Chapter 7 Regular Expression

#?zero or one times
import re

batRegex = re.compile(r'Bat(wo)?man') #similar to Batwoman|Batman which is also one(wo) or zero time
mo = batRegex.search('The Adventures of Batman')
mo.group()
print(mo.group()) #mo will not match if 'The Adventures of Batmanmanman'; it will be equals to false

#*One or zero times
superRegex = re.compile(r'Super(wo)*man') #Can appear Zero or more times
moo = superRegex.search('The Adventures of Superwowowoman')
moo.group()
print(moo.group())

#+One or more times (must appear at least once
catRegex = re.compile(r'Cat(wo)+man') #Cat(wo) can appear one or more times;
mooo = catRegex.search('The Adventures of Catwowowoman') #not optional to remove 'wo'
print(mooo.group())

#Escaping '+*?'
regex = re.compile(r'(\+\*\?)+') #Match these one or more times
reg = regex.search('I learned about +*?+*?+*? regex syntex')
print(reg.group())

#match specific number of repetitions {x} (exactly x)
haRegex = re.compile(r'(Ha){3}') #Match 'Ha' that repeats exactly 3 times
ha = haRegex.search('He said "HaHaHa"')
print(ha.group())

#greedy and nongreedy matching; greedy=  longest string ; non-greedy(?) = shortest string
digitRegex = re.compile(r'(\d){3,5}?') #without ? is greedy; with ? is non-greedy
digitz = digitRegex.search('1234567890')
print(digitz.group())

#shorthand character classes \d ; \w ; \s
import re
lyrics = ''' 11 pipers piping,
10 lords a leaping, 
9 ladies dancing, 
8 maids a milking , 
7 swans a swimming ,
6 geese a laying ,
5 golden rings,
4 calling birds '''

xmasRegex = re.compile(r'\d+\s+\w+')
print(xmasRegex.findall(lyrics))

#Making own character classes
 #r'(a|e|i|o|u)'
vowelRegex = re.compile(r'[aeiouAEIOU]') #for lowercase,  r'[a-z] ; for uppercase, r'[A-Z]
DoublevowelRegex = re.compile(r'[aeiouAEIOU]{2}') #two vowels in a row
print(vowelRegex.findall('Robocop eats baby food. '))
print(DoublevowelRegex.findall('Robocop eats baby food. '))

# ^ Negative character classes
consonantsRegex = re.compile(r'[^aeiouAEIOU]') # ^ will make negative character class,
print(consonantsRegex.findall('Robocop eats baby food. ')) # which means anything that is not 'aeiouAEIOU'

# ^ string begins with 'Hello'
beginsWithHelloRegex = re.compile(r'^Hello') #doesn't count if 'Hello' is in the middle of the string
hello = beginsWithHelloRegex.search('Hello there James!')
print(hello.group())

# $ string ends with 'World'
endsWithWorldRegex = re.compile(r'world!$')
world = endsWithWorldRegex.search('Hello world!')
print(world.group())

# ^\d+$ for both begin and ends with
beginEndwithdigit = re.compile(r'^\d+$') #which means begin with a digit and ends with a digit
digitzz = beginEndwithdigit.search('23949592') #The entire string must be digits
print(digitzz.group())

#anything except newline
atRegex = re.compile(r'.at') # .  anything followed by at
print(atRegex.findall('Cat that sat on the flat mat'))
#notice that lat is not in full string because r.at is only expecting 1 char.
#to change that
atRegex = re.compile(r'.{1,2}at') #one or two character followed by at
print(atRegex.findall('Cat that sat on the flat mat'))

#dot star to match anything (.*)
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
print(nameRegex.findall('First name: Daphne Last name: Chuah'))

#(.*?)non greedy (.*)greedy     # matches any character except new line character
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>') #nongreedy
greedy = re.compile(r'<(.*)>') #greedy
print(nongreedy.findall(serve))
print(greedy.findall(serve))

#re.DOTALL
prime = 'Serve the public trust.\nProtect the innocent. \nUpload the law.'
dotStar = re.compile(r'.*', re.DOTALL) #everything including new lines #greedy match
star = dotStar.search(prime)
print(star.group())

#re.IGNORECASE
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) #or re.I
print(vowelRegex.findall('I enjoy food'))

#sub()
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

#\1, \2, etc in sub()
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))

#re.VERBOSE - multilines & comments
re.compile(r'''
(\d\d\d-)|      #area code (without parens,with dash)
(\(\d\d\d\)  )   #-or- area code with parens and no dash
\d\d\d           #first 3 digits 
-                   #second dash
\d\d\d\d           #last 4 digits
\sx\d{2,4}    #extension, like x1234''', re.VERBOSE)
