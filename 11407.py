from sys import stdin

def phi(n, raiz, mem):
    ans = 0
    if n in mem:
        ans = mem[n]
    else:
        if n == raiz * raiz: ans = 1
        elif raiz == 1: ans = n
        else:
            tmp =  n - (raiz * raiz)
            seguir = phi(tmp, (int((tmp)**(0.5))), mem) + 1
            ignorar = phi(n, raiz-1, mem)
            ans = min(seguir, ignorar)
        mem[n] = ans           
    return ans

def main():
    mem = {}
    inp = int(stdin.readline())
    for _ in range (0, inp):
        n = int(stdin.readline())
        print(phi(n, int(n**(0.5)), mem))
    
main()