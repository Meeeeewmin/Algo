N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1

small = abs(arr[start] + arr[end])

pos1, pos2 = start, end
flag = True

if arr[start] > 0 :
    # print(f"{arr[start]} {arr[start+1]}")
    pos1, pos2 = start, start+1
    flag = False

if arr[end] < 0 :
    pos1, pos2 = end-1, end
    flag = False

while start < end and flag:

    temp = arr[start] + arr[end]
    if small > abs(temp):
        small = abs(temp)
        pos1, pos2 = start, end
    
    if temp < 0 :
        start += 1
    elif temp > 0:
        end -= 1
    else:
        break
    
print(f"{arr[pos1]} {arr[pos2]}")

'''
5
-99 -2 -1 4 98

-99  98



4
-100  -2  -1  103

-2  -1

'''