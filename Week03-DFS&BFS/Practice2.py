# 이코테
# 미로탈출
# Sol : BFS 유형 : (1,1) 부터 BFS를 이용하여 모든 노드를 큐에 넣기 > 노드 방문 시 이전 노드의 거리에 +1 하기

from collections import deque

# 입력
n, m = map(int, input().split())
graph = []
for i in range(n):
    # 띄어쓰기 없이 입력
    graph.append(list(map(int, input())))


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 로 노드 방문
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 갈 수 없는 길인 경우
            if graph[nx][ny] == 0:
                continue

            # 방문하지 않은 노드인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))