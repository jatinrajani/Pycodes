import re
count=0
total=0
y=list()
fhand=open('mbox')
for line in fhand:
     x=re.findall('^New .*: ([0-9]+)' ,line)
     if len(x)>0:
          x=map(int,x)
          r=x[0]
          y.append(r)
          count=count+1
total=sum(y)
print total
print count
(average)=total/float(count)
print average
