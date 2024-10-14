from sys import stdin

def phi(profits, K):
    i, suma = 0, 0
    while i < K:
        if profits[i] > 0: suma += profits[i]
        i += 1
    suma += sum(profits[i:])
    return suma

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        N, K = map(int, stdin.readline().split())
        xi = list(map(int, stdin.readline().split()))
        yi = list(map(int, stdin.readline().split()))
        profits = []
        for j in range(N):
            profit = yi[j] - xi[j]
            profits.append(profit)
        profits.sort()
        ans = phi(profits, K)
        if ans <= 0: print(f"Case {i+1}: No Profit")
        else: print(f"Case {i+1}: {ans}")
main()