import requests
from bs4 import BeautifulSoup
import datetime

def gettitle(x):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={x}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)
    return 

def gettitle_session(x):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={x}'
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)
    return 

# no session 0:00:34.047784
# with session 0:00:12.933128
if __name__ == '__main__':
    s = requests.session()
    start = datetime.datetime.now()
    for x in range(1,21):
        gettitle_session(x)
    finish = datetime.datetime.now() - start
    print(finish)
