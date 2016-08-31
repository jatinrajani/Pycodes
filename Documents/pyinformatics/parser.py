import string
count=dict()
fname=open("romeo")
for line in fname:
    line=line.translate(None,string.punctuation)
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in count:
            count[word]=1
        else:
            count[word]=count[word]+1
print count
