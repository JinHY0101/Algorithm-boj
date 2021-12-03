N, M = map(int,input().split())
A=[list(map(int,input())) for _ in range(N)]
B=[list(map(int,input())) for _ in range(N)]
cnt=0
def reverse(a,b):
    for i in range(a,a+3):
        for j in range(b,b+3):
            A[i][j]=1-A[i][j]
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            reverse(i,j)
            cnt+=1

if A==B:
    print(cnt)
else:
    print(-1)

"""
문제 정의
행렬 A를 B로 바꾸는데 필요한 연산의 횟수 최소 값
모든 원소를 뒤집는다

모르는 포인트 타겟을 어떻게 잡을지?
단순히 BFS로 풀리는것 같아 보이지는 않음
"""