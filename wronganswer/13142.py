from sys import stdin

def biseccion(f, a, b, v):
    low, hi, eps, ans = a, b, 1e-6, None
    while (hi-low) > eps:
        mid = low+(hi-low)/2
        if v <= f(mid): hi = mid
        else: low = mid
    ans = low
    return ans

def f(v):
    ans = v / 11.57407407
    return ans

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        T, S, D = map(int, stdin.readline().split())
        d = D/T
        if D > 0:
            ans = int(biseccion(f, 0, D, d))
            if ans == 0:
                print(f'Add {ans} tons')
            else: print(f'Remove {ans} tons')
        else:
            ans = int((biseccion(f, D, 0, d)*(-1)))
            print(f'Add {ans} tons')

main()

