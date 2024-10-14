from sys import stdin
import math

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

def kruskal(n, aristas, numT):
  for i in range(n): makeSet(i)
  aristas.sort(key = lambda x: x[2])
  mst, i = [], 0
  while i < len(aristas) and len(mst) < n-numT:
    u, v = aristas[i][0], aristas[i][1]
    if findSet(u) != findSet(v):
      unionSet(u, v)
      mst.append(aristas[i][2])
    i += 1
  return mst

def main():
    global p, rango
    cases = int(stdin.readline())
    for _ in range(cases):
        numT = int(stdin.readline())
        sensores = []
        sensor = list(map(int, stdin.readline().split()))
        while sensor[0] != -1:
            sensores.append(sensor)
            sensor = list(map(int, stdin.readline().split()))
        aristas = []
        for i in range(len(sensores)-1):
            for j in range(i+1, len(sensores)):
                dist = math.sqrt(((sensores[j][0]-sensores[i][0])**2)+((sensores[j][1]-sensores[i][1])**2))
                aristas.append((i, j, dist))
        p, rango = [0 for _ in range(len(sensores))], [0 for _ in range(len(sensores))]
        mst = kruskal(len(sensores), aristas, numT)
        ans = math.ceil(mst[-1])
        print(ans)
        p, rango = None, None

main()
        