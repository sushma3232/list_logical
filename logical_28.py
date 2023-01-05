a=["one","two","three"]
i=0
while i<len(a):
    print(i+1,":",a[i])
    i=i+1
    
    
# output-
# 1:one
# 2:two
# 3:three


a="my name is indhu"
b=a.split()
print(b)
i=0
c=" "
d=[]
while i<len(b):
    c=c+b[i]+"_"
    i=i+1
print(c)
