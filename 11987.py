from sys import stdin

p, r, c, s, ref, count = None, None, None, None, None, None

def makeSet(n):
    global p, r, c, s, ref
    p[n], r[n], c[n], s[n], ref[n]  = n, 0, 1, n+1, n

def findSet(n):
    global p
    ans = None
    if n == p[n]: ans = n
    else:
        p[n] = findSet(p[n])
        ans = p[n]
    return ans

def unionSet(u, v):
    global p, r, c, s
    u, v = ref[u], ref[v]
    pU, pV = findSet(u), findSet(v)
    if pU != pV:
        if r[pU] < r[pV]: 
            p[pU] = pV
            s[pV] += s[pU] 
            c[pV] += c[pU]  
        elif r[pU] > r[pV]: 
            p[pV] = pU
            s[pU] += s[pV]
            c[pU] += c[pV]
        else:
            r[pV] += 1
            p[pU] = pV
            s[pV] += s[pU]
            c[pV] += c[pU]

def move(u, v):
    global p, r, c, s, ref, count
    orU, u, v = u+1, ref[u], ref[v]
    pU, pV = findSet(u), findSet(v)
    if pU != pV:
        if pU == u and r[u] == 0: unionSet(u, v)
        elif r[u] >= 1:
            ref[count], ref[u] = count, count
            p.append(count)
            r.append(0)
            c.append(1)
            s.append(orU)
            c[pU] -= 1
            s[pU] -= orU
            unionSet(count, v)
            count += 1
        else:
            c[pU] -= 1
            s[pU] -= orU
            p[u] = u
            unionSet(u, v)

def res(u):
    u = ref[u]
    pU = findSet(u)
    ans = c[pU], s[pU]
    return ans
        
def main():
    global p, r, c, s, ref, count
    inp = stdin.readline()
    while(inp != '' and inp != '\n'):
        n, m = map(int, inp.split())
        p = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        c = [0 for _ in range(n)]
        s = [0 for _ in range(n)]
        ref, count = {}, n
        for i in range(n): makeSet(i)
        for _ in range(m):
            tmp = stdin.readline().split() 
            if len(tmp) == 3: 
                op, u, v = map(int, tmp)
                u, v = u-1, v-1
            else: 
                op, u = map(int, tmp)
                u = u-1
            if op == 1: unionSet(u, v)
            elif op == 2: move(u, v)
            else: print(res(u)[0], res(u)[1])
        p, r, c, s, ref, count = None, None, None, None, None, None
        inp = stdin.readline()
    
main()