def listmult(numlist):
     themul=1
     for i in numlist:
          themul=themul*i
     return themul
x=[]
while True:
     y=raw_input("enter number")
     
     if y=="Done":
          break
     else:
          y=int(y)
          x.append(y)
y=listmult(x)
print y
