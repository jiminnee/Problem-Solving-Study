# 이코테 3-2
# 큰 수의 법칙
# M의 크기가 큰 경우
# Sol : 첫 번째로 큰 수와 두 번재로 큰 수는 특정 수열 형태로 일정하게 반복 > 반복되는 수열 파악

# 입력
n,m,k = map(int, input().split())
num_list = list(map(int, input().split()))

# 가장 큰 2개의 수 찾기
num_list.sort()
first = num_list[n-1]
second = num_list[n-2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k # (수열이 반복되는 횟수) * K = 가장 큰 수가 더해지는 횟수
count += m % (k+1) # 나누어 떨어지지 않는 경우 > 나머지만큼 가장 큰 수를 더해주어야 함

# 첫번째로 큰 수와 두번째로 큰 수 차례대로 더하기
result = 0
result += count * first
result += (m-count) * second

print(result)