

"""
Use try and except block to handle connection errors.

If you run the code without an Internet connection, instead of getting a bunch of errors, 
you should get a print statement like

“Connection failed. Please make sure you’re connected to the Internet!”
"""

import requests

def INTERNET_CONNECTION(url):
    try:
        requests.get(url)
        print('You are connected to the internet')
    except requests.exceptions.RequestException:
        print('Connection failed. Please make sure you\'re connected to the Internet.')

INTERNET_CONNECTION("https://www.google.com")
