
k=int(input('卡拉茲'))
B=int(k)
N=int(1)
if k%2==0 and k!=1:
    k=int(k/2)
if k%2==1 and k!=1:
    k=int(3*k+1) 
if k>B:
    B=k
N=N+1
print(k)
