"""
+ x / -

BFS로?
우선 시간 복잡도 고려X 시도
"""
from collections import deque

s, t = map(int,input().split())
visited=[]

if s==t:
    print(0)
    exit()

def BFS():
    global s,t
    q=deque()
    q.append((s,''))

    while q:
        #a는 숫자 b는 기호
        num,v=q.popleft()
        visited.append(num)
        if num==t:
            print(v)
            return
        for op in ('*','+','/'):
            if op=='*':
                new_num=num*num
            elif op=='+':
                new_num=num+num
            else :
                new_num=1
            if 0 <= new_num <= t and new_num not in visited:
                visited.append(new_num)
                q.append((new_num,v + op))
    print(-1)

BFS()       

    

"""
현재 해결이 안되는 점 
어떻게 접근할지
BFS에 str정보를 어떻게 저장할지    
    
"""