import urllib
size=0
x=urllib.urlopen('http://songs1.djmazadownload.com/music/indian_movies/Mohenjo%20Daro%20(2016)/04%20-%20Tu%20Hai%20-%20Mohenjo%20Mohenjo%20[DJMaza.Desi].mp3')
sng=open('tu hai.mp3','w')
while True:
     info=x.read(100000)
     if len(info)<1:
          break
     size=size+len(info)
     sng.write(info)
print size
sng.close()
