#I have used Python language to solve this 4th problem

p=[1,2,3,4,5,6,7,8,9]
q=[]
r={}
n = int(input("Enter number of elements : "))

for i in range(0, n):
    s = int(input())
    q.append(s)

for i in range(len(p)):
    count=0
    for j in range(len(q)):
        if(q[j]%p[i]==0):
            count+=1
        r[p[i]]=count
print(r)