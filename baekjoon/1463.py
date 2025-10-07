f = int(input())

def check(x,cnt):

    if(x > f):
        return cnt

    r1 = check(x*3, cnt+1)
    r2 = check(x*2, cnt+1)
    r3 = check(x+1, cnt+1)

    return min(r1,r2,r3)


result = check(1, 0)
print(result)