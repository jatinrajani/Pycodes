def reverse(a):
     if len(a)==1:
          return a[0]
     else:
          return reverse(a[1:len(a)+1])+a[0]
x=raw_input("enter string")
z=str(x)
print reverse(z)
