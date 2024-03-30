# 이코테 3-2
# 큰 수의 법칙
# Sol : 첫 번째로 큰 수를 K만큼 더한 후, 두 번째로 큰 수를 1번 더하기

# 입력
n,m,k = map(int, input().split())
num_list = list(map(int, input().split()))

# 가장 큰 2개의 수 찾기
num_list.sort()
first = num_list[n-1]
second = num_list[n-2]

result = 0
while True:
    # 첫 번째로 큰 수를 k만큼 더하기 (k 이상 초과할 수 없으므로)
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break

    # 두 번째로 큰 수는 한번만 더하기
    result += second
    m -= 1

print(result)

