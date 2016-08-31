#using recursion for multiplication
def listmult(numlist):
     mult=1
     if len(numlist)==1:
          return numlist[0]
     else:
          mult=mult*numlist[0]*listmult(numlist[1:])
          return mult
print (listmult([1,4,9]))
          
