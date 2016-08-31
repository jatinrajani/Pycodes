fhand=open('romeo')
x=dict()
count =0
for line in fhand:
    words=line.split()
    for i in words:
       x[i]='m'
       
print x


fhand=open('romeo')
for line in fhand:
    words=line.split()
    for i in words:
        count=count+1
print count

    
