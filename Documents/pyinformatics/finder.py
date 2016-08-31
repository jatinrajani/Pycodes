import re
hand=open('mboxshort')
for line in hand:
     line=line.rstrip()
     if re.search('^From:.+@',line):
          print line
