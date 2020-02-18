from lxml import html
import requests

page = requests.get('https://econofin-bsi.blogspot.com/2019/11/t10a1-analise-de-mercado-de-acoes.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
title = tree.xpath('//h3[@class="post-title entry-title"]/text()')

print('Users: ', title)