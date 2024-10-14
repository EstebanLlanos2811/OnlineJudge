from sys import stdin

p, rango = None, None

def makeSet(v):
    p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)
    if u != v:
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1

def kruskal(n, aristas):
    global p, rango
    p, rango = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
    for i in range(1, n + 1): makeSet(i)
    mst, i = [], 0
    while i < len(aristas) and len(mst) < n-1:
        u, v, c = aristas[i][0], aristas[i][1], aristas[i][2]
        if findSet(u) != findSet(v):
            unionSet(u, v)
            mst.append(c)
        i += 1
    return mst

def phi(n, aristas):
    global p, rango
    slim = float('inf')
    while len(aristas) >= n-1:
        mst = kruskal(n, aristas)
        if len(mst) == n-1:
            tmp = mst[-1]-mst[0]
            if tmp < slim: slim = tmp
        aristas.pop(0)
    return slim

def main():
    global p, rango
    n, m = map(int, stdin.readline().split())
    while n != 0:
        aristas, ans = [], 0
        for _ in range(m):
            u, v, c = map(int, stdin.readline().split())
            aristas.append((u, v, c))
        aristas.sort(key = lambda x: x[2])
        if m < n-1: ans = -1
        else: 
            ans = phi(n, aristas)
            if ans == float('inf'): ans = -1
        print(ans)
        n, m = map(int, stdin.readline().split())

main()