#!/usr/bin/env python
# -*- coding: utf-8 -*-

__auther__ = 'hea1er'

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

searchURL = ''
search_template = 'http://www.baidu.com/s?id=utf-8&wd={0}&pn={1}'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

def URLCrawler(searchURL):
    try:
        request = Request(searchURL, headers = headers)
        response = urlopen(request)
        bsObj = BeautifulSoup(response, 'lxml')
        
        for h3 in bsObj.findAll('h3'):
            try:
                links = h3.children
                for link in links:
                    if 'href' in link.attrs:
                        findlink = getRealURL(link.attrs['href'])
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
        response = urlopen(request)
        return response.geturl()
    except HTTPError as e:
        return None

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