import sys 
from collections import deque

N = int(sys.stdin.readline())
queque= deque()

for _ in range (N) :
    word = sys.stdin.readline().split()
    if word[0] == "push" :
        queque.append(word[1])
    elif word[0] =="top" :
        print(queque[-1])
    elif word[0] =="pop" :
        if len(queque)==0:
            print(-1)
        else :
            print(queque.popleft())
    elif word[0]=="size" :
        print(len(queque))
    elif word[0]=="empty":
        if len(queque)==0:
            print(1)
        else : 
            print(0)
    elif word[0]=="front" :
        if len(queque)==0 : print(-1)
        else :
            print(queque[0])
    elif word[0]=="back" :
        if len(queque)==0 : print(-1)
        else :
            print(queque[-1])

