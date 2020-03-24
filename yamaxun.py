import requests

url = 'https://www.amazon.cn/dp/B07DQBFQ2D/ref=lp_888502051_1_15?s=pc&ie=UTF8&qid=1585016366&sr=1-15'

try:
    r = requests.get(url)
    r.raise_for_status()
    print(r.headers)
    print(r.encoding)
    print(r.text)
except:
    print(r.status_code)
    print(r.headers)
    print(r.encoding)
    print(r.apparent_encoding)


print('====================================================')
print('\n')
print('====================================================')

ua = {'user-agent':'Mozilla/5.0'}
try:
    new_r = requests.get(url,headers=ua)
    new_r.raise_for_status()
    print(new_r.headers)
    print(new_r.status_code)
    print(new_r.encoding)
    print(new_r.apparent_encoding)
    new_r.encoding = new_r.apparent_encoding 
    print(new_r.text)
except:
    print('Error')
