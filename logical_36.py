a=[1,2,3,4,5,6]
i=0
b=-1
c=[]
while i<3:
    c.append(a[b])
    c.append(a[i])
    i=i+1
    b=b-1
print(c)
# output:[6,1,5,2,4,3]