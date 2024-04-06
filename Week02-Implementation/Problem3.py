# 이코테 실전문제 03
# 게임 개발
# Sol : 시뮬레이션 - 방향을 정하는 리스트를 먼저 만든 후 for 문을 돌리자!

# 입력
n, m = map(int, input().split())
x, y, d = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방문한 위치를 저장하기 위한 맵 - 0으로 초기화
location = [[0] * m for _ in range(n)]
# 맨 처음 위치를 방문 처리
location[x][y] = 1

# 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향으로 회전하기 위한 함수
def turn_left():
    global d # 함수 밖에서 사용된 전역변수 이므로 global 처리 해줘야 함
    d -= 1
    if d == -1:
        d = 3

result = 1
count = 0
while True:
    # 현재 방향을 기준으로 왼쪽 방향으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 왼쪽 방향에 가보지 않은 칸이 있다면 이동
    if location[nx][ny] == 0 and array[nx][ny] == 0:
        location[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        count = 0
        continue
    # 네 방향 모두 가본 칸이거나 바다로 되어 있는 칸인 경우
    else:
        count += 1
    # 모두 갈 수 없는 경우
    if count == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있는 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        count = 0

print(result)
