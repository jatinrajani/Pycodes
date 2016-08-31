#converting file to upper case
fname=raw_input("enter file name\n")
try:
    fhand=open(fname)
except:
    print 'File cannot be opened'
    exit()
for line in fhand:
    print line.upper()
