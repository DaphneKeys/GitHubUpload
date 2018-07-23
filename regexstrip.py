#!python3
# Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
import re

sentence = input('Enter your sentence: ')
charneedstoremove = input('Enter character you would like to remove from your sentence: \n')

def stripper(Usersentence, CharacterRegex):
    if charneedstoremove != '':
        charReplace = re.sub(CharacterRegex, r'', Usersentence)
        print('Result after character removed:')
        print(charReplace)
    else:
        print('No character to remove:')
        SpaceReplace = re.sub(r'^\s$', r'', Usersentence)
        print(SpaceReplace)

stripper(sentence,charneedstoremove)