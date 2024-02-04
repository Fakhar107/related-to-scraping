import requests
import csv
import concurrent.futures
# these codelines are to be run to see what all proxies in the list are working
proxylist = []

with open('proxylist.csv','r') as f:
    
    def extract(proxy):
         with concurrent.futures.ThreadPoolExecutor( )as exector:
            exector.map(extract, proxylist)