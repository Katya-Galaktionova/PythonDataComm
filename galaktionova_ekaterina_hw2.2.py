
"""
Write a program that gets the current time from  the US navy:
https://tycho.usno.navy.mil/timer.html
Use urllib
Use a function to get the time.
Display the time in MDT, EDT and AKDT.
Compare the time in minutes to your local  computer time. If they do not match, 
print that your local computer time is off.
"""
import urllib.request
import re
import ssl
from time import strftime

ssl._create_default_https_context = ssl._create_unverified_context

def DISPLAY_PAGE(URL):
    PAGE = urllib.request.urlopen(URL)
    PAGE_TEXT = PAGE.read().decode('utf8')
    SEARCH_TIME = re.findall(r'\d.\:\d.\:\d.\ .M\ (?:MDT|EDT|AKDT)', PAGE_TEXT)
    print(SEARCH_TIME)
    SEARCH_TIME_MIN = int(re.search(r'(?<=:)\d.', str(SEARCH_TIME)).group())
    if int(strftime("%M")) != SEARCH_TIME_MIN:
        print('Local computer time is off')
    else:
        print('There is a match!')           

DISPLAY_PAGE("http://tycho.usno.navy.mil/timer.html")

