import csv
import re
count=0

x=open('j.csv','r')
csv_f=csv.reader(x)
for row in csv_f :
     count=count+1
     print "mobile no." +row[1]
print count
