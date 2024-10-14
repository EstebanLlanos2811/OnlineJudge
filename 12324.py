from sys import stdin

T, B, mem = None, None, None

def phi(t, b):
    global mem
    ans, key = None, (t, b)
    if key in mem: ans = mem[key]
    else:
        if t == len(T): ans = 0
        elif b >= len(T)-t: ans =  phi(t+1, b+B[t]-1)+(T[t]>>1)
        elif b == 0: ans = phi(t+1, B[t])+T[t]
        else: ans = min(phi(t+1, (b+B[t])-1)+(T[t]>>1), phi(t+1, b+B[t])+T[t])
        mem[key] = ans
    return ans

def main():
    global T, B, mem
    trips = int(stdin.readline())
    while trips != 0:
        T, B, mem = [], [], {}
        for _ in range(trips):
            ti, bi = map(int, stdin.readline().split())
            T.append(ti)
            B.append(bi)
        if sum(B) == 0: print(sum(T))
        else: print(phi(0, 0))
        T, B, mem = None, None, None
        trips = int(stdin.readline())

main()
        


