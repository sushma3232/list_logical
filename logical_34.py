a=[1,2,3,4,5,6]
i=0
count=0
while i<len(a)-1:
    if a[i]-a[i+1]==-1:
        count+=1
    i+=1
print(count)
if count==len(a)-1:
    print("true")
else:
    print("false")
    
    
    
    
    
    
    
    