import requests
import csv
# this code is to check if csv list is working with this code or not
proxylist = []

# r is read only arguement and f refers as file
with open('proxylist.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

print(len(proxylist))
