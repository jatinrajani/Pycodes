# counting number of From
count=0
file_name = raw_input("Enter a file name: ")
fhand=open(file_name)
for line in fhand:
    words=line.split()
    
    if line.startswith("From"):
        count=count+1
        print words[1]
print count
