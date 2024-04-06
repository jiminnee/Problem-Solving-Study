# 이코테 4-1
# 상하좌우
# Sol : 시뮬레이션 유형 - 이동 횟수에 비례하여 연산

# 입력
n = int(input())
x, y = 1, 1
moves = input().split()

# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 방향 차례로 확인
for move in moves :

    # L, R, U, D 차례로 확인
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 맵을 벗어난 경우 무시
    if nx < 1 or ny <1 or nx >n or ny >n :
        continue

    x,y = nx, ny

print(x,y)