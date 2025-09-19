import time
import requests
from bs4 import BeautifulSoup
import lxml
from datetime import datetime
from selenium import webdriver as wd


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 OPR/121.0.0.0 (Edition std-2)'
accept = 'text/html'

headers = {'Accept': accept,
           'User-Agent': user_agent}


def parser_nasa():
    url_nasa = 'https://science.nasa.gov/mission/voyager/voyager-1/'
    req_nasa = requests.get(url_nasa, headers)
    soup = BeautifulSoup(req_nasa.text, 'lxml')
    soup_main = soup.find('body').find('main', class_='site-main')
    table = soup_main.find('div', class_='grid-col-12 desktop:grid-col-6 padding-left-0 desktop:padding-left-10')
    date = table.find_all('div', class_='p-lg font-weight-bold margin-0 padding-0 line-height-sm')[1].text
    month, number, year = date.split()
    new_date = f'{month[:3]} {number.strip(' ,')} {year}'
    date_object = datetime.strptime(new_date, "%b %d %Y")
    format_date = date_object.strftime('%Y%m%d')
    return format_date


def parser_rfc():
    url_rfc = 'https://datatracker.ietf.org/doc/rfc1149/history/'
    req_rfc = requests.get(url_rfc, headers)
    soup = BeautifulSoup(req_rfc.text, 'lxml')
    table = soup.find('tbody')
    last_raw = table.find_all('tr')[-1]
    first_column = last_raw.find('td')
    format_date = first_column.text.strip().replace('-', '')
    return format_date


def parser_loc():
    browser = wd.Chrome()
    url_loc = 'https://search.catalog.loc.gov/instances/9acb1e70-9ea7-5ec1-9e9e-4d1e8b6d865e?option=title&pageNumber=1&query=The%20C%20programming%20language&recordsPerPage=25'
    browser.get(url_loc)
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    isbn = soup.find('div', class_='recordMetadata__content recordMetadata__isbnContent')
    isbn_10 = isbn.find_all('li')[1]
    return isbn_10.text


def parser_unicode():
    url_unicode = 'https://www.unicode.org/Public/UNIDATA/UnicodeData.txt'
    req_unicode = requests.get(url_unicode, headers)
    rows = req_unicode.text.split('\n')
    for row in rows:
        code, name, *other = row.split(';')
        if name == 'BRAIN':
            return code


def parser_bitcoin():
    url_btc = 'https://www.blockchain.com/explorer/blocks/btc/0'
    req_btc = requests.get(url_btc, headers)
    soup = BeautifulSoup(req_btc.text, 'lxml')
    text = soup.find('div', class_='sc-d60e75c0-7 iwMRhg').text
    date = text.split()[2:5]
    date_object = datetime.strptime(' '.join(date), '%B %d, %Y')
    format_date = date_object.strftime('%Y%m%d')
    return format_date


voyager_date = parser_nasa()
rfc1149_date = parser_rfc()
brain_codepoint = parser_unicode()
btc_genesis_date = parser_bitcoin()
kr2_isbn10 = parser_loc()
result = 'FLAG{' + f'{voyager_date}-{rfc1149_date}-{brain_codepoint}-{btc_genesis_date}-{kr2_isbn10}' + '}'
print(result)
