import requests
from bs4 import BeautifulSoup

url = 'http://www.python123.io/ws/demo.html'

r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())

for tag in soup.find_all(True):
    print(tag.name)
    print('\n')
    print(tag.attrs)
    print('\n')
    print(tag.string)
    print('\n')
    print(tag)







