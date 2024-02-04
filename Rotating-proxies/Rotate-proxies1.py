import requests

proxy = '220.150.76.27:3128'

try:

    r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=3)
    print (r.json())

except:
    print('failed')
    pass