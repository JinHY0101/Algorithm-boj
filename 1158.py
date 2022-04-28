import sys 
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
list=[]
q = deque([i+1 for i in range(N)])

while len(q) !=0 :
    q.rotate(-K)
    list.append(q.pop())

print('<' + ', '.join(map(str, list)) + '>')
