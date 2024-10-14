from sys import stdin

def binSearch(iter, p, Y, aMax):
    low, hi, limS = iter, len(p), (p[iter] + Y) - 1
    while low + 1 < hi:
        mid = (low + hi) // 2
        if p[mid] <= limS: low = mid
        else: hi = mid
    if aMax[0] < (low - iter) + 1:
        aMax[0] = (low - iter) + 1
        aMax[1] = p[iter]
        aMax[2] = p[low]
    return aMax[0], aMax[1], aMax[2]

def popes(Y, p):
    aMax = [0, 0, 0]
    for i in range(len(p)): ans = binSearch(i, p, Y, aMax)
    return ans
    
def main(): 
    inp = stdin.readline()
    while inp != "\n" and inp != "":
        Y = int(inp)
        P = int(stdin.readline())
        p, ans = [], 0
        while len(p) != P: p.append(int(stdin.readline()))
        ans = popes(Y, p)
        print(ans[0], ans[1], ans[2])
        stdin.readline()
        inp = stdin.readline()

main()