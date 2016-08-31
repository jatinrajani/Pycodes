count=0
average=0
total=0
while True:  
        try:
            y=raw_input('Enter number')
            count=count+1
            if y=='Done':
                count=count-1
                break
            total=total+int(y)
            average=total/count
        except:
            count=count-1
            print "enter valid number"
            
print total
print average
print count

