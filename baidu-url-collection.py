#!/usr/bin/env python
# -*- coding: utf-8 -*-

__auther__ = 'hea1er'

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

searchURL = ''
search_template = 'http://www.baidu.com/s?id=utf-8&wd={0}&pn={1}'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

def URLCrawler(searchURL):
    try:
        request = Request(searchURL, headers = headers)
        response = urlopen(request, timeout = 5)
        bsObj = BeautifulSoup(response, 'lxml')
        
        for h3 in bsObj.findAll('h3'):
            try:
                links = h3.children
                for link in links:
                    if 'href' in link.attrs:
                        findlink = getRealURL(link.attrs['href'])
                        if 'gov' in findlink or findlink == '':
                            print('The government or None')
                        else:
                            print(findlink)
                            writeFile(findlink)
            except AttributeError as e:
                print(e)
            else:
                continue
        
    except HTTPError as e:
        print(e)

def getRealURL(findlink):
    try:
        request = Request(findlink, headers = headers)
        try:
            response = urlopen(request, timeout = 5)
            return response.geturl()
        except Exception as e:
            return ''
    except HTTPError as e:
        return ''

def writeFile(findlink):
    with open('url.txt', 'a') as f:
        f.write(findlink + '\n')

if __name__ == '__main__':
    query = input('Using Google Hacking to query:\n')
    amount = input('The number of pages:\n')
    pages = int(amount) * 10
    page = 0
    while page <= pages:
        searchURL = search_template.format(query, page)
        URLCrawler(searchURL)
        page += 10