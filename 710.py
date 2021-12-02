N, K = map(int,input().split())
A=[]
for _ in range(N) : A.append(int(input()))

l=len(A)-1 #뒤에서부터 읽어주기 위한 좌표
cnt=0
while True:
    if K==0:
        print(cnt)
        break
    if K>=A[l]:
        K=K-A[l]
        cnt+=1
    else :
        l=l-1
    
    

    



"""
문제 정의
N개의 동전으로 가치의 합을 K개로 만드려고한다.
그 최소값을 구하는 문제
입력 정보:
N K 
동전개수 N개 만큼 오름 차순으로
--------------------------
배열에 저장
큰수부터 나눈다.

10-11 10분
"""