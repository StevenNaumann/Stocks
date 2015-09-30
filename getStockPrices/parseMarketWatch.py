from lxml import html
import requests

page = requests.get('http://finance.yahoo.com/q/hp?s=TSLA+Historical+Prices')
tree = html.fromstring(page.text)

data = tree.xpath('//td[@class="yfnc_tabledata1"]/text()')

print 'data: ', data
