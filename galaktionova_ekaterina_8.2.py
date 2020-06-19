#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read urls from the urls.csv file (uploaded on canvas)
Access the urls using requests and BeautifulSoup modules
Using a multi-threaded approach fetch the title of the webpages 
and the links of embedded images in each of those pages. (Title 
within the HTML)
Insert URLs and corresponding titles in a new “results.csv” file. 
Include the file in your submission
"""

from bs4 import BeautifulSoup
import requests
import threading
        
def get_urls():
    with open('urls.csv') as fh:
        urls = []
        for row in fh:
            urls.append(row.strip())
        del urls[0]
        return urls
 
def access_url(url, results):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    img_src = []
    for link in soup.find_all('img'):
        img_src.append(link.get('src'))
    results.append((url, soup.title.string))
  
def create_threads(urls, results):
    ts = []
    for url in urls:
        t = threading.Thread(target = access_url, args = (url, results))
        t.start()
        ts.append(t)
    return ts

def wait_threads(ts):
    for t in ts:
        t.join()
        
def save_to_file(results):
    output = open('results.csv', 'w') 
    for line in results:
        output.write(str(line[0]) + ', ' + str(line[1]) + '\n')   
    output.close()     


if __name__=='__main__':
    results = []
    readdata = get_urls()
    threads = create_threads(readdata, results)
    wait_threads(threads)
    save_to_file(results)