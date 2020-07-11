import requests
from lxml import html
from urllib.parse import urljoin
import csv

resp = requests.get(url='https://coinmarketcap.com/', headers={
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
})
print(resp)
tree = html.fromstring(html=resp.content)

coins_main = tree.xpath("//tbody/tr[@class='cmc-table-row']")[0]

for coin in coins_main:
    c = {
        'Name': coin.xpath("."),
        'Market_cap': coin.xpath("."),
        'Price': coin.xpath("."),
        'Change(24)': coin.xpath(".")
        
    }
print(coins_main)