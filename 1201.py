"""
문제정의

3구간으로 나눈다 
4  

5 4 3 1
1  4 3 2 8 7 6 5 13 12 11 10
13
5개가 된다
8 % 3
3
5 % 3
2

3 

3




"""
import math
N, M, K  = map(int,input().split())
q=N-K
s=[]
s.append(K)

if N < M+K-1 or N > M*K:
    print(-1)
    exit()

for i in range(M-1,0,-1):
    if i==1:
        s.append(q)
        continue
    tmp = math.ceil(q / i)
    =q-tmp
    s.append(tmp)

start=0
for i in range(len(s)):

    for j in range(start+s[i],start,-1):
        print(j,end=" ")
    start=start+s[i]
