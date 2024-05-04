# 이코테
# 바이러스

# 입력 (정점, 간선의 수)
v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    #간선의 시작점과 끝점 입력받음
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, cnt):
    result[x] = True
    for node in graph[x]:
        if not result[node]:
            cnt = dfs(node, cnt+1)
    return cnt

result = [False for _ in range(v+1)]
print(dfs(1, 0))