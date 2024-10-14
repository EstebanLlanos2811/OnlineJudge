from sys import stdin, setrecursionlimit

setrecursionlimit(100000)

res = None

def solve(pIz, pDer, v):
    global res
    ans = None
    if (pIz[0]+pDer[0]) == v[0] and (pIz[1]+pDer[1]) == v[1]: ans = (pIz, pDer, v)
    else:
        if ((pIz[0]+pDer[0])*v[1]) > (v[0]*(pIz[1]+pDer[1])):
            res.append('L')
            ans = solve(pIz, (pIz[0]+pDer[0], pIz[1]+pDer[1]), v)
        else:
            res.append('R')
            ans = solve((pIz[0]+pDer[0], pIz[1]+pDer[1]), pDer, v)
    return ans

def main():
    global res
    m, n = map(int, stdin.readline().split())
    while m != 1 and n != 1:
        res = []
        solve((0, 1), (1, 0), (m, n))
        res = ''.join(res)
        print(res)
        res = None
        m, n = map(int, stdin.readline().split())

main()
        