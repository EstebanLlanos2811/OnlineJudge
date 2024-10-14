from sys import stdin

def solve(hippos, N, H, Ta, Td):
    ans, low, hi = 0, 0, N - 1
    while low <= hi:
        if hippos[low] + hippos[hi] < H and low != hi and (2 * Ta) + 1 > Td:
            ans += Td
            hi -= 1
            low += 1
        else:
            ans += Ta
            hi -= 1
    return ans

def main():
    n = int(stdin.readline())
    for i in range(n):
        N, H, Ta, Td = map(int, stdin.readline().split())
        hippos = list(map(int, stdin.readline().split()))
        hippos.sort()
        print(f"Case {i + 1}:", solve(hippos, N, H, Ta, Td))

main()