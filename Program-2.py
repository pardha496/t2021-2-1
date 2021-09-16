#I have used Python language to solve this 2nd problem

n=int(input()) 
o=1
l=[]
for i in range(n):
    l.append(o)
    o+=2
print(*l,sep=",")