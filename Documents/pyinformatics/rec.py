def conv_int_string(a,base):
     s="012345789
     if a<base:
          d=str(a)
          return d
     else:
          return conv_int_string(a/base,base)+str(a%base)
          
print (conv_int_string(199,10))
