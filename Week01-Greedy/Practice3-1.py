# 이코테 3-1
# 거스름돈
# Sol : 가장 큰 화페부터 돈을 거슬러 주기 (가장 큰 단위가 작은 단위의 배수이므로)

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
