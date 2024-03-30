# 이코테 실전문제 04
# 1이 될 때까지
# Sol : K 값으로 최대한 많이 나누기, 나누는 것이 불가능하다면 1 빼기

# 입력
n,k = map(int, input().split())

result = 0
while n >= k:
    while n%k != 0: # K로 나누는 것이 불가능한 경우
        n -= 1
        result += 1

    # K로 나누는 것이 가능한 경우 최대한 나누기
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)