from sys import stdin

def binSearch(n):
    low, hi = 1, n+1
    while low+1 != hi:
        mid = low + ((hi - low) >> 1)
        if mid*mid <= n: low = mid
        else: hi = mid
    return low*low


def main():
    n = int(stdin.readline())
    while n != 0:
        print(binSearch(n))
        n = int(stdin.readline())
        
main()