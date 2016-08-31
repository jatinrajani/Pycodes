#computing the grades
score=raw_input("please enter your score")
sc=float(score)
if sc>=0.9 and sc<=1.0:
    print "A"
elif sc>=0.8 and sc<=1.0:
     print "B"
elif sc>=0.7 and sc<=1.0:
     print "C"
elif sc>=0.6  and sc<=1.0:
     print "D"
elif sc<0.6 and sc <=1.0:
    print "F"
else:
    print "enter valid score"
