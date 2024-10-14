from sys import stdin
import heapq

def modRaiz(dic, dicR):
    valorRaiz = dic[0][0]
    valorDic = dicR[dic[0][2]]
    valorRaiz += valorDic
    pRaiz, psRaiz, vRaiz = heapq.heappop(dic)
    nuevaRaiz = (valorRaiz, psRaiz, vRaiz)
    nuevaRaiz = heapq.heappush(dic, nuevaRaiz)
    return dic

def main():
    T = int(stdin.readline())
    dic, dicR = [], {}
    for _ in range(T):
        n, k = map(int, stdin.readline().split())
        for i in range(n):
            name, frec = stdin.readline().split()
            frec = int(frec)
            dic.append((frec, i, name))
            dicR[name] = frec
        heapq.heapify(dic)
        for _ in range(k):
            print(dic[0][0], dic[0][2])
            modRaiz(dic, dicR)
        dic, dicR = [], {}

main()