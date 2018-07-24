#! python3
# downloadXkcd.py

import requests, os, bs4

url = 'https://xkcd.com/' #url variable that starts 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True) #make directory named 'xkcd' , if the directory exist, permission remain unchanged

while not url.endswith('#'): #ends the loop when url ends with '#'
    #Download the page.
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text) #store html into soup

    #Find the URL of the comic image
    comicElem = soup.select('#comic > img') #selector of image
    if comicElem == []: #if selector of image is empty
        print('Could not find comic image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src') #from comicElem, get src element //imgs.xkcd.com/comics/___.png
        #Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        #Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb') #open file path 'xkcd', name of files (rock.png) , write binary mode
        for chunk in res.iter_content(100000): #save to downloaded file to hard drive 
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href')

print('Done.')
