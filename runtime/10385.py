from sys import stdin

def compC(dPie):
    tComp = []
    for i in range(len(A) - 1): tComp.append(dPie/A[i][0] + (T - dPie) / A[i][1])
    compR = min(tComp)
    compT = dPie / A[-1][0] + (T - dPie) / A[-1][1]
    return (compR - compT) * 3600

def terSearch(low, hi):
    eps = 10**-6
    mid1 = low + (hi - low) / 3
    mid2 = hi - (hi - low) / 3
    if hi - low < eps: ans = [round(compC((hi + low) / 2)), (hi + low) / 2, T-((hi + low) / 2)] 
    if compC(mid1) > compC(mid2): ans = terSearch(low, mid2)
    elif compC(mid1) < compC(mid2): ans = terSearch(mid1, hi)
    return ans

def main():
    global T, A
    line = stdin.readline()
    while line != "":
        if len(line) == 1: line = stdin.readline()
        T = int(line)
        n = int(stdin.readline())
        A = []
        while len(A) != n:
            x = stdin.readline().split()
            A.append((float(x[0]), float(x[1])))
        ans = terSearch(0, T)
        if ans[0] < 0.0: print('The cheater cannot win.')
        else: print('The cheater can win by {0} seconds with r = {1:.2f}km and k = {2:.2f}km.'.format(ans[0], ans[1], ans[2]))
        stdin.readline()
        line = stdin.readline()

main()
