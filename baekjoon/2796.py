# 브루트 포스 : 모든 경우를 탐색해야하는 문제. 

from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 0

for cards in combinations(nums, 3):
    if sum(cards) <= M:
        result = max(result, sum(cards))

print(f"{result}")

