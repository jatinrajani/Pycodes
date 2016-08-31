import socket
import re
url=raw_input("Please enter url")
x=re.findall('^h\S.*://(\S.*)/\S.*/\S.*.txt$',url)
print x
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
     mysock.connect((x[0],80))
except:
     print "please enter correct url"
z='GET ' +url +' HTTP/1.0\n\n'
try:
     mysock.send(z)
except:
     print "sorry can't be connected"
while True:
     data=mysock.recv(512)
     if (len(data)<1):
          break
     print data
mysock.close()
  
