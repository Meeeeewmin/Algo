def insert(idx, num, arr):
    temp = []
    for i in range(len(arr)):        
        if i == idx:
            temp.append(num)
        else:
            temp.append(arr[i])
    arr[:] = temp

def erase(idx, arr):
    # arr[:] = arr
    arr[:] = arr[:idx] + arr[idx+1:]

arr = [1,2,3,4,5,6]

insert(3, 50, arr)
erase(4, arr)

print(arr)
print(arr[3:])

temp = (1,2)
temp2 = (3,4)
temp = temp + temp2
print(temp)