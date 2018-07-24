#!python3
#link verification
#http://inventwithpython.com/page_that_does_not_exist
import requests
while True: 
    web = input('Enter a URL of a web page(the program will stop if the webpage is invalid): ')
    web = requests.get(web)

    try:
        web.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        break
                    
    if web.raise_for_status() != 404:
        print('It is a valid Url') 
        continue
