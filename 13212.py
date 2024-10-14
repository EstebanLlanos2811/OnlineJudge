from sys import stdin

inv, tmp = 0, []

def inp():
    global inv, tmp
    nArr = int(stdin.readline())
    while(nArr != 0):
        arr, inv = [], 0
        tmp = [ None for _ in range(nArr) ]
        for _ in range(nArr): arr.append(int(stdin.readline()))
        print(mergesort(arr, 0, nArr))
        nArr = int(stdin.readline())

def mergesort(A, low, hi):
    if low + 1 < hi:
        mid = low + ((hi-low)>>1) 
        mergesort(A, low, mid)
        mergesort(A, mid, hi)
        merge(A, low, mid, hi)
    return inv

def merge(A, low, mid, hi):
    global tmp, inv 
    for i in range(low, hi): tmp[i] = A[i]
    l, r = low,mid
    for n in range(low, hi):
        if l == mid: A[n], r = tmp[r], r+1 
        elif r == hi: A[n], l = tmp[l], l+1 
        else:
            if tmp[l] <= tmp[r]: A[n], l = tmp[l], l+1
            else:
                A[n], r = tmp[r], r+1
                inv += (mid - l)
inp()