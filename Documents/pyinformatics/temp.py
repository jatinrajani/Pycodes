# converting temperature from farenheit to celsius
try:
    faren=raw_input("enter the temperature in farenheit\n")
    float(faren)
    celsius=((float(faren)-32)*5)/9
    print "here is your converted temperature "
    print celsius
except:
    print "please enter a number"
