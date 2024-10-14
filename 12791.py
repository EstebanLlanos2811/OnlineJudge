from sys import stdin

def lap(x, y, low, hi):
    ans = None
    while low + 1 != hi:
        mid = low + ((hi - low)>>1)
        tx = x*mid
        ty = y*(mid-1)
        if tx == ty: ans = mid
        elif tx < ty: hi = mid
        elif tx > ty: low = mid
    mid = low + ((hi - low)>>1)
    tx = x*mid
    ty = y*(mid-1)
    if low + 1 == hi:
        if tx <= ty: ans = mid
        else: ans = hi
    return ans

def inp():
    inp = stdin.readline()
    while inp != "\n" and inp != "":
        x, y = map(int,inp.split())
        print(lap(x, y, 2, y))
        inp = stdin.readline()

inp()