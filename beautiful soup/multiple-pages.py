from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

data_lists = []

for x in range(1, 18):
    url = f"https://priceoye.pk/mobiles?page={x}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    products = soup.select('div.productBox')

    for p in products:
        
        title = p.select_one('div.p-title').text.strip()
        price = p.select_one("div.price-box").text.replace('Rs.','').strip()
        
        data_dict = {
            'titles': title,
            'prices': price,
            
        }
        data_lists.append(data_dict)  
    print(f'No. of mobiles on page-{x}: ',len(data_lists))
    time.sleep(2)
df = pd.DataFrame(data_lists)
print(df.head())
df.to_csv('mobiles.csv')
