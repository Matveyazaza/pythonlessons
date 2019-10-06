import requests
from bs4 import BeautifulSoup
#def temp(html):#
    #return html.find ('div', {'style' : 'link__condition day-anchor i-bem'}).text#
def temp(html):
    return html.find ('div', {'style' : 'color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px'}).text
url = 'https://www.kinopoisk.ru/top/lists/1/'
response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml') 
print ('Рейтинг фильма "Побег из Шоушенка" составляет ', temp(html))