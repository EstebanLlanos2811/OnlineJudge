from sys import stdin

def solve(A, k):
    low, hi = max(A), sum(A)
    while low < hi:
        mid = low+((hi-low)>>1)
        if f(mid, A) <= k: hi = mid
        else: low = mid+1
    return low

def f(x, A):
    ans, sum, i = 1, 0, 0
    while i < len(A):
        if sum+A[i] <= x: sum += A[i]
        else:
            sum = A[i]
            ans += 1
        i += 1
    return ans

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        n, m = map(int, stdin.readline().split())
        A = list(map(int, stdin.readline().split()))
        lim = solve(A, m)
        res, sum, i, j, sep, count = [], 0, -1, 0, m-1, 0
        while j < len(A):
            if sep == 0: res.insert(0, f"{A[i]}")
            elif sep == n-count:
                res.insert(0, "/")
                res.insert(0, f"{A[i]}")
                sep -= 1
                count += 1
            elif sum+A[i] <= lim:
                sum += A[i]
                res.insert(0, f"{A[i]}")
                count += 1
            else:
                res.insert(0, "/")
                res.insert(0, f"{A[i]}")
                sum = A[i]
                sep -= 1
                count += 1
            i -= 1
            j += 1
        print(' '.join(res))

main()