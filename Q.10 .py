a=[]
b=int(input("enter the num:-"))
i=0
while i<b:
    c=[]
    d=int(input("enter the num:"))
    j=0
    while j<d:
        e=int(input("enter th enum:-"))
        c.append(e)
        j=j+1
    a.append(c)
    i=i+1
print(a) 
k=0  
while k<len(a):
        l=0
        f=a[k][0]
        while  l<len(a[k]):
            if a[k][l]>f:
                f=a[k][l]
            l=l+1
        print(f)
        k=k+1        
    
