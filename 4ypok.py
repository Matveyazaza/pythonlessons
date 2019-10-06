import requests
from bs4 import BeautifulSoup
from datetime import datetime
url='https://www.cbr.ru/scripts/XML_daily.asp?'
response = requests.get(url)
soup = BeautifulSoup (response.content, 'lxml')
def get_course(id):
    return soup.find('valute', {'id': id} )
usd = get_course('R01235')
print (usd)