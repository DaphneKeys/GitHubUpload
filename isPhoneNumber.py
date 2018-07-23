#automate the boring stuff with python (page148)
#chapter 7
def isPhoneNumber(text):
    if len(text) != 12: #if length of text  not exactly of equals to 12
        return False
    for i in range(0,3): #checks first 3 character
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #if [3] is not '-'
        return False
    for i in range(4,7):#checks for 5th to 7th character
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
#detect if there is any phone numbers in the string
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12] #starting from i up to i+12
    if isPhoneNumber(chunk):
        print('Phone number found: '+chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number')