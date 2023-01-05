
# remove zero's
a=["16800","16700","30","20"]
b=[]
for i in a:
    while i[-1]=="0":
        i=i[:-1]
    b.append(i)
print(b)



