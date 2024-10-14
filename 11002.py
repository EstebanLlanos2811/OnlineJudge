from sys import stdin

N, A, mem = None, None, None

def cPosibles(i, j):
    ans = None
    if i > N-1: ans = [j, j+1]
    else: 
        if j == 0: ans = [j]
        elif j == len(A[i])-1: ans = [j-1]
        else: ans = [j-1, j]
    return ans

def phi(i, j, s):
    ans, key = None, (i,j,s)
    if key in mem: ans = mem[key]
    else:
        if i == 0: ans = abs(A[i][j]) == abs(s)
        else:
            ans, c, k = False, cPosibles(i, j), 0
            while ans == False and k < len(c):
                if len(c) == 1: ans = phi(i-1, c[0], s+A[i][j]) or phi(i-1, c[0], s-A[i][j])
                elif len(c) == 2: ans = phi(i-1, c[0], s+A[i][j]) or phi(i-1, c[0], s-A[i][j]) or phi(i-1, c[1], s+A[i][j]) or phi(i-1, c[1], s-A[i][j])
                k += 1
        mem[key] = ans
    return ans

def solve():
    ans, n, f = None, 0, False
    while f == False:
        f = phi(2*N-2, 0, n)
        if f == True: ans = n
        n += 1
    return ans

def main():
    global mem, A, N
    N = int(stdin.readline())
    while N != 0:
        A, mem = [[]], {}
        for i in range(2*N - 1):
            A[i] = list(map(int, stdin.readline().split()))
            if i < 2*N-2: A.append([])
        print(solve())
        N, A, mem = None, None, None
        N = int(stdin.readline())
 
main()