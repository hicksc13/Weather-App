from bs4 import BeautifulSoup
import requests
def get_craigslist_price(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('body > section > section > h1 > span > span.price')
    return elems[0].text
def get_craigslist_name(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#titletextonly')
    return elems[0].text


productUrl = "https://springfield.craigslist.org/ele/d/ava-rick-morty/7565431188.html"

price = get_craigslist_price(productUrl)
name = get_craigslist_name(productUrl)



print(f"The name is " + name + ' and it costs: ' + price)




