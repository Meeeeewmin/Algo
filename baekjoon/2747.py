# 피보나치 수열 in python
import sys
input = sys.stdin.readline
N = int(input())


d = [0]*(N+1)

if N == 1 or N== 2:
    print("1")
else:
    d[1] = 1
    d[2] = 1
    for i in range(3, N+1):
        d[i] = d[i-1] + d[i-2]
    print(d[N])



'''
def pibo(n):
    if n == 1 or n == 2:
        return 1

    return pibo(n-1) + pibo(n-2) 

result = pibo(N)

print(result)
'''