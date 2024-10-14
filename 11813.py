from sys import stdin

INF = float('inf')

def dijkstra(G, s):
    dist = [INF]*len(G)
    dist[s] = 0
    pqueue = [(dist[s], s)]
    while pqueue:
        du, u = pqueue.pop(0)
        for v, duv in G[u]:
            if du+duv < dist[v]:
                dist[v] = du+duv
                pqueue.append((dist[v], v))
    return dist

def universe(N): return (1<<N)-1

def is_elt(n, X): return (X|(1<<n)) == X

def remove_elt(n, X): return X-(1<<n) if is_elt(n, X) else X

def singleton(n, X): return X == (1<<n)

def phi(N, w, u, X, mem):
    ans, key = None, (u, X)
    if key in mem: ans = mem[key]
    else:
        if not(is_elt(u, X)): ans = INF
        elif singleton(u, X): ans = w[0][u]
        else:
            ans, Y = INF, remove_elt(u, X)
            for v in range(1, N):
                if is_elt(v, Y):
                    ans = min(ans, phi(N, w, v, Y, mem)+w[v][u])
        mem[key] = ans
    return ans

def tsp(N, w):
    ans = INF
    X = remove_elt(0, universe(N))
    mem = dict()
    for u in range(1, N): ans = min(ans, phi(N, w, u, X, mem)+w[u][0])
    return ans

def main():
    T = int(stdin.readline())
    for _ in range(T):
        n, m = map(int, stdin.readline().split())
        G = [[] for _ in range(n)]
        for _ in range(m):
            X, Y, D = map(int, stdin.readline().split())
            G[X].append((Y, D))
            G[Y].append((X, D))
        S = int(stdin.readline())
        stores = [0]
        for _ in range(S):
            s = int(stdin.readline())
            stores.append(s)
        stores.sort()
        dist = []
        for i in stores: dist.append(dijkstra(G, i))
        cG = [[] for _ in range(len(dist))]
        for i in range(len(dist)):
            for j in range(len(dist[i])):
                if j in stores: cG[i].append(dist[i][j])
        print(tsp(S+1, cG))

main()