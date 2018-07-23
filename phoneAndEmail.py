#! python3
#Extracting phone numbers and email address #included country code for phone numbers
import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# +1-9185842555 , 415-555-0000, 555-000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
([+\d]+                               #country code (optional)
[\w|\s])?                             #seperator for country code (optional) 
((\d\d\d)|(\(\d\d\d\)))?              # area code (optional) - this can appear zero or one times
(\s|-)                                #first seperator
\d\d\d                                #first 3 digits
-                                     #seperator 
\d\d\d\d                              #last 4 digits
(((ext(\.)?\s)|x)                     # extension word-part (optional)  
(\d\{2,5}))?                          #extension number-part(optional) - \d{2,5} -> can appear 2 to 5 times
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[\w_.+]+        #name part- similar to a-zA-Z0-9
@                      #@ symbol
[\w_.+]+        #domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()  # return the string from the clipboard

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extraced email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
