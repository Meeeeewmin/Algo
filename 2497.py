# 수열 codepass
N, M = map(int, input().split())
arr = list(map(int,input().split()))
sum = 0

for i in range(M):
    sum += arr[i]

result = sum
for i in range(M,N):
    sum = sum + arr[i] - arr[i-M]
    if result < sum:
        result = sum

print(result)

'''
10 3
3 -2 -4 -9 0 3 7 13 8 -3
0. 1  2  3 4 5 6  7 8. 9

0~2
- 0 + 3
1 + 4

'''