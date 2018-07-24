#This program retrieve the price of a product from amazon

import bs4
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
def getAmazonPrice(productUrl):

    res = requests.get(productUrl)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newOfferAccordionRow .header-price')
    return elems[0].text.strip()


price = getAmazonPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=tmm_pap_swatch_0?_encoding=UTF8&amp;qid=&amp;sr=')
print('The price is ' + price)
