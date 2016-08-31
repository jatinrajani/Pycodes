str = 'X-DSPAM-Confidence: 0.8475'
spos=str.find(' ',0,len(str))
print spos
epos=str.find('5',spos,len(str))
print epos
add=str[spos+1:epos+1]
print add
