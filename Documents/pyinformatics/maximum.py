# calculating the minimum and maximum values
def maximum(values):
    
    largest=None
    for value in values:
        
        if value>largest:
            largest=value
        print 'Loop:',value,largest
    print largest
values=[1,5,7,9]
maximum(values)
