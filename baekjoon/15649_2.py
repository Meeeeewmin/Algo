N, M = map(int, input().split())


def backtracking():
    if (len(arr) == M):
        print(' '.join(map(str, arr)))
        return

    for n in range(1,N+1):
        if n in arr:
            continue
        arr.append(n)
        backtracking()
        arr.remove(n) # pop 으로 변경 **


arr = []
backtracking()