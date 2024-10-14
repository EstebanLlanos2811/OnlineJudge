from sys import stdin

arr = [1, 1]
res = 0

def fibonacci():
    global arr
    a, b = 0, 1
    c = a + b
    count = 0
    while count < 38:
        a = b
        b = c
        c = a + b 
        arr.append(c)
        count += 1
    arr.pop(0)

def binSearch(low, hi, x):
    ans = None
    if low == hi: ans = 0
    elif low+1 == hi: ans = low+1
    else: 
        mid = low+((hi-low)>>1)
        if arr[mid] < x and arr[mid+1] > x: ans = mid
        elif arr[mid] == x: ans = mid-1
        elif arr[mid] > x: ans = binSearch(low, mid, x)
        else: ans = binSearch(mid, hi, x)
    return ans

def solve(x):
    global res
    n = len(arr)
    tmp, tmp2 = x, binSearch(0, n, x)
    if tmp == 0: ans = 0
    else:
        while tmp != 1:
            res += int('1' + ('0' * tmp2), 2)
            tmp -= arr[tmp2]
            tmp2 = binSearch(0, n, tmp)
        ans = res
    return ans

def main():
    global res
    T = int(stdin.readline())
    fibonacci()
    for _ in range(T):
        n = int(stdin.readline())+1
        print(bin(solve(n))[2:])
        res = 0
        
main()