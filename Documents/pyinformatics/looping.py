def looping(word,letter):
    count =0
    for i in word:
        if i==letter:
            count=count+1
    print count
x=raw_input('enter word')
y=raw_input("enter letter")
looping(x,y)
