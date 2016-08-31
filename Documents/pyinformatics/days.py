import string
day=dict()
fname=open("mboxshort")
for line in fname:
   x=line.find("From",0,len(line))
   print line
