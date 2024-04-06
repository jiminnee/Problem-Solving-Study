# 이코테 실전문제 02
# 왕실의 나이트
# Sol : 나이트가 이동 가능한 경로를 하나씩 확인하기 (맵을 벗어나지 않도록 유의)

# 입력
location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

# 이동 방향
move_types = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동 방향 차례로 확인
result = 0
for move in move_types:
    next_row = row + move[0]
    next_column = column + move[1]

    # 맵 안에 있는 경우
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)