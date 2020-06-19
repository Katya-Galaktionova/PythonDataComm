#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This URL lists top 500 websites on the Internet:
https://moz.com/top500

-Access it using requests, and parse the first 100 website URLs mentioned in the website. 
(Of course you will have to filter URLs that contain moz.com)

-Using multithreading, connect to these top 100 websites and get all their titles. 
Save this data in a new csv file named “extra.csv”

"""


from bs4 import BeautifulSoup
import requests
import threading
        
def get_urls():    
    rowdata = requests.get('https://moz.com/top500/domains/csv').text
    lines = rowdata.split('\n')
    elements = []
    for line in lines[1:100]:
        elements.append(line.split(','))
    urls = []
    for i in elements:
        urls.append(i[1])
    print(urls)
    return[]
 
def access_url(url, results):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
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
    output = open('extra.csv', 'w') 
    for line in results:
        output.write(str(line[0]) + ', ' + str(line[1]) + '\n')   
    output.close()     


if __name__=='__main__':
    results = []
    readdata = get_urls()
    threads = create_threads(readdata, results)
    wait_threads(threads)
    save_to_file(results)