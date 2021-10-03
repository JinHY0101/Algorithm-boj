import sys 
sys.setrecursionlimit(10000) 


R, C = map(int, input().split()) 
S = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
K = [0]*26 
K[S[0][0]] = 1 
ans = 1 

def DFS(x, y, cnt): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    now = (x, y) 
    global ans 
    ans = max(ans, cnt) 
    for i in range(4): 
        nx = now[0] + dx[i] 
        ny = now[1] + dy[i] 
        if 0 <= nx < R and 0 <= ny < C and K[S[nx][ny]] == 0: 
                K[S[nx][ny]] = 1 
                DFS(nx, ny, cnt+1) 
                K[S[nx][ny]] = 0 

DFS(0, 0, ans) 
print(ans)


    


