# 이코테 실전문제 03
# 숫자 카드 게임
# Sol : 각 행에서 가장 작은 수 뽑기 > 그 중에서 가장 큰 수 뽑기

# 입력
n,m = map(int, input().split())

result = 0
for i in range(n):
    num_list = list(map(int, input().split()))
    # 각 행에서 가장 작은 수를 뽑고, 그 중 가장 큰 수 뽑기
    min_num = min(num_list)
    result = max(result, min_num)

print(result)