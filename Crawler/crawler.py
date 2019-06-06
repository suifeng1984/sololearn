
import requests
from bs4 import BeautifulSoup

# myHtml=requests.get('https://www.baidu.com').content
#
# soup = BeautifulSoup(myHtml,'html.parser')
#
# links = soup.findAll('a')
# for link in links:
#     print(link.string)


data = requests.get('https://www.baidu.com').content

soup = BeautifulSoup(data,'html.parser')

print(soup.body.div.attrs)