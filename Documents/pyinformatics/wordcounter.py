import re
count=0
fhand=open('mbox')
m=raw_input('enter word which has to be searched')
for line in fhand:
     line=line.rstrip()
     lst=re.findall(m,line)
     if len(lst)>0:
          count=count+1
print count
