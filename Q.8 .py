# a=[]
# b=int(input("enter the num:-"))
# i=0
# while i<=b:
#     c=int(input("enter the num:-"))
#     a.append(c)
#     i=i+1
# print(a)
# d=[]
# e=int(input("enter the num:-"))
# j=0
# while j<e:
#     f=int(input("enter the num:-"))
#     d.append(f)
#     j=j+1
a= [1, 5, 10, 12, 16, 20]
d = [1, 2, 10, 13, 16]
c=a+d
s=[]
i=0
while i<len(c):
    if c[i] not in s:
        s.append(c[i])
    i=i+1
print(s)             