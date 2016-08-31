import re
fhand=open('mbox')
for line in fhand:
     ine=line.rstrip()
     x=re.findall('^X\S.*: ([0-9.]+)',line)
     if len(x)>0:
          print x
