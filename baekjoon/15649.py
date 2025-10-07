from itertools import combinations
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

def backtracking():
    if len(arr) == M:
        print(" ".join(map(str, arr)))

    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

arr = []
backtracking()

# for cards in combinations(range(1,N+1), M):
#     for i in range(M):
#         print(f"{cards[i]}", end=" ")
#     print("")
