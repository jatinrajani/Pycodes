# calculating average Dspam confidence
filename=raw_input("enter file name\n")
count=0
total=0
average=0
try:
    fhand=open(filename)
except:
    print "Enter valid file name"
    exit()
for line in fhand:
    if line.find('X-DSPAM-Confidence:')==-1:
        continue
    else:
        spos=line.find('X-DSPAM-Confidence:')
        y=line[spos+19:len(line)+1]
        z=float(y)
        total=total+z
        count=count+1
        average=total/count
print total
print average
