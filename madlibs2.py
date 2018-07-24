content = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
wordssplit = content.split()
wordsDictionary = {k:v for k,v in enumerate(content)} #same thing as below
#wordsDictionary = {k:v for k,v in k,v in content.items()} 
check = ["ADJECTIVE", 'NOUN', 'ADVERB', 'VERB']

for keys,values in wordsDictionary:
    for checkspeech in check:
        if checkspeech in values:
            print('Enter an {}:'.format(values.lower())) #ADJECTIVE,NOUN,ADVERB,VERB is lowercase
            wordsDictionary[keys] = input()

print(' '.join(wordsDictionary.values()))
