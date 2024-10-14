from sys import stdin

N, L, C = 0, 0, 0

def phi(inpS):
    cL, cC, i = 0, 0, 0
    while i < len(inpS):
        if cC + (inpS[i] + 1) <= C:
            cC += inpS[i] + 1
            i += 1
        elif cC + inpS[i] == C:
            cL += 1
            cC = 0
            i += 1
        else:
            cL += 1
            cC = 0
    if cC != 0: cL += 1
    cP = cL / L
    if cP % 1 != 0: cP = int(cP) + 1
    else: cP = int(cP)
    return cP

def main():
    global N, L, C
    inp = stdin.readline()
    while inp != "\n" and inp != "":
        N, L, C = map(int, inp.split())
        inpS = list(map(len, stdin.readline().split()))
        print(phi(inpS))
        inp = stdin.readline()
main()
