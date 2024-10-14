from sys import stdin

mem = {}

def phi(platos, p, n):
    if (p, n) in mem: ans = mem[(p, n)]
    else:
        if n <= 0: ans = 0
        elif p == 0: ans = float('inf')
        else: ans = min(phi(platos, p-1, n-platos[p-1])+platos[p-1], phi(platos, p-1, n))
        mem[(p, n)] = ans
    return ans
    
def main():
    global mem
    cases = int(stdin.readline())
    for _ in range(cases):
        n = int(stdin.readline())
        p = int(stdin.readline())
        platos = list(map(int, stdin.readline().split()))
        mem = dict()
        ans = phi(platos, p, n)
        if ans == float('inf'): print("NO SOLUTION")
        else: print(ans)
        mem = None

main()

