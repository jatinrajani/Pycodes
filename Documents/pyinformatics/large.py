m=list()
largest=None
while True:
    i=raw_input("enter the number")
    if i=="Done":
        break
    z=float(i)
    m.append(z)
    for z in m:
        if z>largest:
            largest=z
                   
    
print largest    
print m
    
