import urllib
from BeautifulSoup import *
url=raw_input("Enter link")
html=urllib.urlopen(url)
soup=BeautifulSoup(html)
tags=soup('a')
for tag in tags:
     print 'TAG:', tag
     print 'url:' ,tag.get('href',None)
     print 'Content' ,tag.contents[0]
     print 'attrs' ,tag.attrs
