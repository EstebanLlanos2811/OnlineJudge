from sys import stdin

mem, s = None, None

def phi(n, x, coalitions):
    ans, key = None, (n, x)
    if key in mem: ans = mem[key]
    else:
        if x > 50: ans = s/x
        elif n == len(coalitions): ans = 0
        else: ans = max(phi(n+1, x+coalitions[n], coalitions), phi(n+1, x, coalitions))
        mem[key] = ans
    return ans

def main():
    global mem, s, N
    N, X = map(int, stdin.readline().split())
    while N != 0 and X != 0:
        coalitions = []
        for _ in range(N): coalitions.append(float(stdin.readline()))
        s, mem = coalitions[X-1], {}
        coalitions.pop(X-1)
        ans = phi(0, s, coalitions)*100
        print("{:.2f}".format(ans))
        mem, s = None, None
        N, X = map(int, stdin.readline().split())

main()
        
        