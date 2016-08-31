#computing sum using list
total=0
count=0
numlist=list()
while(True):
    inp=raw_input("enter number")
    if inp=='Done':
        break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print average,sum(numlist)
