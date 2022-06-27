a=[]
b=int(input("enter the num:-")) 
i=0
while i<=b:
    c=int(input("enter the num:-"))
    a.append(c)
    i=i+1
print(a)    
d=[]
e=int(input("enter the num:-"))
j=0
while j<=e:
    f=int(input("enter tyhe num:-"))
    d.append(f)
    j=j+1
print(d)    
s=[]
k=0
while k<len(a):
    if a[k] in d:
        s.append(a[k]) 
    k=k+1
print(s)           