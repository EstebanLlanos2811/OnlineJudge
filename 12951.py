from sys import stdin, setrecursionlimit

N, C, P, mem = 0, 0, [], dict()

setrecursionlimit(2*(10**5))

def phi(n, bandera):
    global mem
    if (n,bandera) in mem: ans = mem[(n,bandera)]
    else:
        if n == N: ans = 0
        else:
            if bandera == True: ans = max(phi(n+1, True), (phi(n+1, False) - C - P[n]))
            else: ans = max(phi(n+1, False), (phi(n+1, True) + P[n]))
        mem[(n,bandera)] = ans
    return ans

def main():
    global mem,N,C,P
    inp = stdin.readline()
    while inp != "\n" and inp != "":
        N, C = map(int, inp.split())
        P = list(map(int, stdin.readline().split()))
        print(phi(0, True))
        mem = dict()
        inp = stdin.readline()
main()