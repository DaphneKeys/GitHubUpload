#!python3
#lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print('Googling...') #display text while downloading the Google page
res = requests.get('https://www.google.com/search?ei=3tEzW-2dHZaS9QOmpZXoDA&q=cats&oq=cats&gs_l=psy-ab.3..0i67k1j0l9.143071.143917.0.144314.4.4.0.0.0.0.96.282.4.4.0....0...1.1.64.psy-ab..0.4.280...35i39k1j0i131k1j0i131i67k1.0.fvVU-byOwAQ')
res.raise_for_status()

#retrieve top search result link
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Open a browser tab for each result
linkElems = soup.select('.r a') #find all <a> elements
numOpen = min(5, len(linkElems)) #min 5 results, return list of all elemts match selector 
for i in range(numOpen):
    webbrowser.open('http://google.com' +linkElems[i].get('href'))


