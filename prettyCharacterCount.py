#python3
# #display {' ': 7,
#  'A': 1,
#  'I': 1,
#  'a': 3,
#  'b': 1,
#  'c': 1,
#  'd': 2,
#  'g': 1,
#  'h': 1,
#  'i': 3,
#  'l': 2,
#  'n': 1,
#  'o': 1,
#  'p': 1,
#  'r': 2,
#  's': 1,
#  't': 2,
#  'w': 1,
#  'y': 1}


import pprint
message = 'It was a bright cold day in April'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)