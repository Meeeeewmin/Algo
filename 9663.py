#N-Queen

import sys
input = sys.stdin.readline

N = int(input())


def queen():
    global result

    if len(arr) == N:
        result += 1
        return

    for n in range(N):
        if n not in arr:
            len_temp = len(arr)
            valid = True
            
            for i in range(len_temp):
                a = arr[i] + len_temp - i
                b = arr[i] - len_temp + i
                if n == a or n == b:
                    valid = False
                    break
            
            if valid:
                arr.append(n)
                queen()
                arr.pop()

arr = []
result = 0
queen()

print(result)
'''
대각선: n-1, n-1
      n+1, n-1
      n-1, n+1
      n+1, n+1

일단 각 행마다 하나씩
      
(0,0)      (0,2)
      (1,1)
(2,0)      (2,2)

[1] [1] [1] [1]

[1]
    [1]
        [1]
            [1]
2, 4, 1, 3
'''