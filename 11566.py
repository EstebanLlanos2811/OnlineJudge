from sys import stdin

N, X, T, K, P, V, mem = 0, 0, 0, 0, [], [], dict()

def phi(n, x, k):
    if (n, x, k) in mem: ans = mem[(n, x, k)]
    else:
        if n == K: ans = 0
        elif k >= 2 and X - ((x + P[n] * 2) * 1.1) >= 0:
            ans = max(phi(n+1, (x + P[n] * 2), k - 2) + (V[n] * 2), phi(n + 1, (x + P[n]) , k - 1) + V[n], 
                      phi(n+1, x, k))
        elif k >= 1 and X - ((x + P[n]) * 1.1) >= 0:
            ans = max(phi(n + 1, (x + P[n]), k - 1) + V[n], phi(n+1, x, k))
        else: ans = phi(n + 1, x, k)
        mem[(n, x, k)] = ans
    return ans

def main():
    global N, X, T, K, P, V, mem
    N, X, T, K = map(int, stdin.readline().split())
    while N != 0 and X != 0  and K != 0:
        X *= (N + 1)
        k = 2 * (N + 1)
        for _ in range(K):
            line = list(map(int, stdin.readline().split()))
            P.append(line[0])
            line.pop(0)
            V.append(sum(line))
        print(f"{phi(0, T*(N+1), k) / (N + 1):.2f}")
        P, V = [], []
        mem = dict()
        N, X, T, K = map(int, stdin.readline().split())
        
main()


        
    