import urllib
x=urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
fhand=open('cover.jpg','w')
fhand.write(x)
fhand.close()
