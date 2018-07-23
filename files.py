#!python3
#Automate the boring stuff with python
#Reading and Writing Plaintext Files
#Test on the interactive shell

helloFile = open('c:\\users\\user\\hello.txt')

#Read mode, only read data, not modify
content = helloFile.read() #Only can read once, therefore assign to content
#helloFile.read() returns 'Hello Alice!\nHow are you?'

print(content)
#Hello Alice!
#How are you?

helloFile.close()

#--------------------#
#readlines() -> lines as strings inside of a list
#read() -> a single string

helloFile = open('c:\\users\\user\\hello.txt')
helloFile.readlines() #['Hello Alice!\n','How are you?']
helloFile.close()

#--------------------#
#write mode 'w' -> overwrite files
#append mode 'a' -> append the text to the end

helloFile = open('c:\\users\\user\\hello2.txt','w')
helloFile.write('Hello!!!!!!!') #returns 12
helloFile.write('Hello!!!!!!!') #returns 12
helloFile.write('Hello!!!!!!!') #returns 12
helloFile.close()

#hello2.txt returns Hello!!!!!!!Hello!!!!!!!Hello!!!!!!!
#notice that there are no new line character, add ourselves

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
import os
os.getcwd() #get current directory to track where is bacon.txt
print(os.getcwd()) #C:\Users\user\AppData\Local\Programs\Python\Python36
baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')

baconFile.close()

#------------------#
#shelve module ->store lists and dictionaries into a binary file
import shelve
shelfFile = shelve.open('mydata') #shelve.open() returns a dictionary-like shelf value
shelfFile['cats'] = ['Zophie','Pooka','Simon','Fat-tail','Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] #returns as a dictionary ['Zophie','Pooka','Simon','Fat-tail','Cleo']
shelfFile.close()

#mydata.bak mydata.dat mydata.dir
#drag mydata.dat to notepad to see binary data file


#keys and values() shelf method
shelfFile = shelve.open('mydata')

list(shelfFile.keys())#returns ['cats']
list(shelfFile.values()) #returns [['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']]



