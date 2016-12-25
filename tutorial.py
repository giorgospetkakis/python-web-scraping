# An online tutorial on web scraping

from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

writer = open('file.txt', 'w')
writer.write(page.content)
writer.close()