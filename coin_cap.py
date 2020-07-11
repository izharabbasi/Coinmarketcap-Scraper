import requests
from lxml import html
from urllib.parse import urljoin
import csv
coins = []

def get(element_list):
    try:
        return element_list.pop(0)
    except:
        return ""

def write_to_csv(data):
    headers = ['Name' , 'Market_cap', 'Price', 'Change(24)']
    with open("coins.csv" , 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(data)


def scraping(url):
    resp = requests.get(url=url, headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    })

    tree = html.fromstring(html=resp.content)

    coins_main = tree.xpath("//tbody/tr[@class='cmc-table-row']")

    for coin in coins_main:
        c = {
            'Name': get(coin.xpath(".//td[2]/div/a/text()")),
            'Market_cap': get(coin.xpath(".//td[3]/div/text()")),
            'Price': get(coin.xpath(".//td[4]/a/text()")),
            'Change(24)':get(coin.xpath(".//td[7]/div/text()"))
            
        }
        coins.append(c)

    next_page = tree.xpath("(//a[@data-qa-id='table-listing-button-next']/@href)[2]")

    if len(next_page) != 0:
        next_page_url = urljoin(base=url, url=next_page[0])
        scraping(url=next_page_url)

scraping(url="https://coinmarketcap.com/")

print(len(coins))

write_to_csv(coins)