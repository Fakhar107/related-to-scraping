from selenium import webdriver
from selenium.webdriver.common.by import By
from selectolax.parser import HTMLParser
import requests

def extract():
    driver = webdriver.Chrome() # extract html with selenium webdriver.
    driver.get('https://books.toscrape.com')
    html = driver.page_source
    driver.close()
    return html

def extract_requests():# Or we can extract html with requests.
    resp = requests.get('https://books.toscrape.com')
    return resp.text

def parse(html):
    html = HTMLParser(html)# selectolax parser is using above 
    # html to parse it to get required information.
    elements = html.css('article')
    for e in elements:
        print(e.text(strip=True))

def main():
    html = extract() #OR html = extract_requests() 
    parse(html)

if __name__ == '__main__':
    main()

