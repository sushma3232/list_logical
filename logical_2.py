l="MahEsH"
i=1
b=[]
c=[]
while i<len(l):
    if l[i].islower():
        b.append(l[i])
    else:
        c.append(l[i])
    i=i+1
print(b)
print(c)




l="MahEsH"
i=0
b=[]
c=[]
while i<len(l):
    if l[i].isupper():
        b.append(i)
    else:
        c.append(i)
    i=i+1
print(b)
print(c)


