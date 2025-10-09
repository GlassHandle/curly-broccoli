def l(x,nodes):
    for j in nodes:
        ans=1
        for i in nodes:
            if i!=j:
                ans*=(x-i)/(j-i)
        basis.append(ans)
node=[0,1,2]
basis=[]
l(1.5,node)
print(basis)
out=[(0,1),(1,3),(2,2)]
ans=0
for i in out:
    ans+=i[1]*basis[i[0]]
print(ans)