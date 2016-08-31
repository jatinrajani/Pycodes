# counting the maximum no. of messages
max=None
x=dict()
fname=open('mboxshort')
for line in fname:
     word=line.split()
     for i in word:
          if i=="From" or i=='From:':
               l=str(word[1])
               if l not in x:
                    x[l]=1
               else:
                    x[l]=x[l]+1 
               
          else:
               continue

def maximum(l):
     k=dict()
     max=None
     m=None
     for i in l:
          z=i.find('@',0,len(i))
          m=str(i[z:len(i)+1])
          print m
          if m not in k:
               k[m]=1
          else:
               k[m]=k[m]+1
          
          if l[i]>max:
               max=l[i]
          
     print max,k
     
maximum(x)
