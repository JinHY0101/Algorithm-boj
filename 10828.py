""""
기능 push pop size empty top
파이썬은 stack 구조를 제공하지 않는다.
기본 클래스 list를 이용하여 stack을 표현한다.
"""
import sys
input= sys.stdin.readline

N = int(input())
stack=[]

for i in range(N):
    command = input().split()

    if command[0]=='push':
        stack.append(command[1])
        
    if command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else : print(stack.pop())              
    if command[0]=='size':
        print(len(stack))
    if command[0]=='empty':
        if len(stack)==0:
            print(1)
        else : print(0)      
    if command[0]=='top':
        if len(stack)==0:
            print(-1)
        else : print(stack[-1])   