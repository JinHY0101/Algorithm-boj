import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for i in tree[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += max(dp[i][0],dp[i][1])
            dp[start][1] += dp[i][0]

n = int(input())
visited = [0 for i in range(n+1)]
tree = [[] for i in range(n+1)]
people = [0]+list(map(int,input().split()))
dp = [ [0,people[i]] for i in range(n+1)] 

for i in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(1)
print(max(dp[1][0],dp[1][1]))


