#I have used Python language to solve this 3rd problem

n=int(input()) 
o=1
l=[]
if(n%2==0):
    for i in range(n-1):
        l.append(o)
        o+=2
    print(*l,sep=",")
else:
    for i in range(n):
        l.append(o)
        o+=2
    print(*l,sep=",")