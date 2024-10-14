from sys import stdin

def conexion(pAcceso, casas, mid):
    ans, puntos, rango = False, 1, casas[0] + mid
    while rango < casas[-1] and puntos < pAcceso:
        for j in range(len(casas)):
            if rango < casas[j] and puntos < pAcceso:
                puntos += 1
                rango = casas[j] + mid
    if rango >= casas[-1]: ans = True
    return ans

def binSearch(casas, pAcceso):
    hi, low = casas[-1], 0
    while low + 1 < hi:
        mid = (low + hi) // 2
        if conexion(pAcceso, casas, mid) == True: hi = mid
        elif conexion(pAcceso, casas, mid) == False: low = mid
    return hi / 2

def main():
    casosPrueba = int(stdin.readline())
    for _ in range(casosPrueba):
        casas = []
        inpC = stdin.readline()
        pAcceso, nCasas = map(int,inpC.split())
        for _ in range(nCasas): casas.append(int(stdin.readline()))
        if pAcceso >= nCasas: print(0.0)
        else:
            casas.sort()
            print(binSearch(casas, pAcceso))
main()