import urllib
count=0
from BeautifulSoup import *
url=raw_input("enter url")
html=urllib.urlopen(url)
soup=BeautifulSoup(html)
tags=soup('a')
for tag in tags:
     print tag
     count=count+1
print count
