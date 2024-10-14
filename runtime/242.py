from sys import stdin

sobre = 0
nCon = 0
mem = dict()
resultado = [-1, [0]]

def phi(c, n):
    global mem
    ans = None
    cams = []
    if n in mem: ans = mem[n]
    else:
        if n == 0: ans = 0
        elif n == c[0]: ans = 1
        elif n < c[0]: ans = 0
        else:
            i = 0
            while i < len(c):
                if c[i] <= n: cams.append(phi(c, n - c[i]) + 1)
                i += 1
            ans = min(cams)
        mem[n] = ans
    return ans

def maximo(res, c):
    global resultado
    if res > resultado[0]:
        ans = [res, c] 
        resultado = [res, c]
    elif res == resultado[0]:
        if len(c) < len(resultado[1]):
            ans = [res, c]
            resultado = [res, c]
        elif len(c) == len(resultado[1]):
            i = -1
            flag = False
            while abs(i) < len(c) and not(flag):
                if c[i] < resultado[1][i]:
                    ans = [res, c]
                    resultado = [res, c]
                    flag = True
                elif c[i] > resultado[1][i]:
                    ans = resultado
                    flag = True
                else: i -= 1
        else: ans = resultado
    else: ans = resultado
    return ans

def imprimir(arr):
    formato = [f"{i:3d}" for i in arr[1]]
    l = f"".join(map(str, formato))
    ans = f"max coverage = {arr[0]:3d} :{l}"
    return ans

def main():
    global sobre, nCon, mem, resultado
    sobre = int(stdin.readline())
    while sobre != 0:
        c = dict()
        nCon = int(stdin.readline())
        for i in range(0, nCon):
            con = list(map(int, stdin.readline().split()))
            c[i] = con[1:]
            j = 1
            ans = phi(c[i], j)
            while  ans <= sobre and ans > 0:
                j += 1
                ans = phi(c[i], j)
            res = j - 1
            resp = maximo(res, c[i])
            mem = dict()
        print(imprimir(resp))
        resultado = [-1, [0]]
        sobre = int(stdin.readline())
main()