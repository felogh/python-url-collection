#!/usr/bin/env python
# -*- coding: utf-8 -*-

__auther__ = 'hea1er'

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

searchURL = ''
apiKey = 'AIzaSyDbmgJ5PK84Nkmf7eHghUcWOpF3l16xqJk'
searchEngineId = '013036536707430787589:_pqjad5hr1a'    #可以申请（这里直接用了网上找到的）
search_template = 'https://www.googleapis.com/customsearch/v1?key={0}&q={1}&cx={2}&fields=items(link)&lr=lang_zh-CN'

def getUrl(searchURL):
    try:
        request = Request(searchURL)
        response = urlopen(request).read().decode('utf-8', 'ignore')
        jsons = json.loads(response)
        urls = jsons['items']
        for url in urls:
            print(url['link'])
    except HTTPError as e:
        print(e)


if __name__ == '__main__':
    query = input('Using Google Hacking to query:\n')
    searchURL = search_template.format(apiKey, query, searchEngineId)
    getUrl(searchURL)