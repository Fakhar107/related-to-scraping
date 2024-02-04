import requests
import csv
# here we are trying to use all the 
#proxies in csv list by below iteration.

proxylist = []

with open('proxylist.csv','r') as f:
    
    def extract(proxy):
        try:
            r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=2)
            print (r.json(), ' - working')
        except:
            pass
        return proxy
    
extract('220.150.76.27:3128')