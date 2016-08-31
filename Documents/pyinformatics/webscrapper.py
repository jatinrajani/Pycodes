import urllib
from BeautifulSoup import *
url=raw_input("enter link")
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
# Retrieve all tags
tags=soup('a')
for tag in tags:
     print tag.get('href',None)
