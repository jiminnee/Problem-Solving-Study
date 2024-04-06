# 이코테 4-2
# 시각
# Sol : 완전 탐색 유형 - 모든 시각을 하나씩 세면서 풀기 (2초 안에 가능하므로 시간 초과 X)

# 입력
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 3이 있는 경우 count 값 1 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)