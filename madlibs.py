#!python3
#madlibs.py
#Automate the boring stuff with python (Page 195)

file = open('MadLibs.txt')
content = file.read()
print(content)
file.close()

#with open('MadLibs.txt') as text:
#    user_input = text.read()

wordssplit = content.split() #['The', 'ADJECTIVE', 'panda', 'walked', 'to', 'the', 'NOUN', 'and', 'then', 'VERB.', 'A', 'nearby', 'NOUN', 'was', 'unaffected', 'by', 'these', 'events.']

wordsDictionary = {k: v for k, v in enumerate(wordssplit)} #retrieve both the index and the value of each item python
#{0: 'The', 1: 'ADJECTIVE', 2: 'panda', 3: 'walked', 4: 'to', 5: 'the', 6: 'NOUN', 7: 'and', 8: 'then', 9:'VERB.', 10: 'A', 11: 'nearby', 12: 'NOUN', 13: 'was', 14: 'unaffected', 15: 'by', 16: 'these', 17: 'events.'}
check_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for keys, values in wordsDictionary.items():
    for cw in check_words:
        if cw in values:
            print('Enter an {}:'.format(values.lower()))#ADJECTIVE,NOUN,ADVERB,VERB is lowercase
            wordsDictionary[keys] = input()

print(' '.join(wordsDictionary.values()))
