import requests
from bs4 import BeautifulSoup


r = requests.get('https://python123.io/ws/demo.html')

print(r.status_code)

print(r.encoding)

print(r.text)


demo = r.text

soup = BeautifulSoup(demo,'html.parser')

print(soup.prettify())


print('====================================================')
print('\n')
print('====================================================')

print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print('====================================================')
print(soup.p)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
