from sys import stdin

def racing(tian, king):
    ans = 0
    while tian != [] and king != []:
        if tian[0] > king[0]:
            ans += 200
            tian.pop(0)
            king.pop(0)
        elif tian[0] == tian[-1]:
            if tian[-1] > king[-1]:
                ans += 200
                tian.pop()
                king.pop()
            elif tian[-1] < king[-1]:
                ans -= 200
                tian.pop()
                king.pop()
            else:
                tian.pop()
                king.pop()
        elif tian[-1] > king[-1]:
            ans += 200
            tian.pop()
            king.pop()
        else:
            ans -= 200
            tian.pop(0)
            king.pop()
    return ans

def main():
    global N
    N = int(stdin.readline())
    while N != 0:
        tian = list(map(int, stdin.readline().split()))
        king = list(map(int, stdin.readline().split()))
        tian.sort()
        king.sort()
        if N == 1:
            if tian[0] > king[0]: print(200)
            elif tian[0] < king[0]: print(-200)
            else: print(0)
        else:
            i, flag = 0, True
            while i < N:
                if tian[i] != king[i]: flag = False
                i += 1
            if flag == True: print(0)
            else: print(racing(tian, king))
        N = int(stdin.readline())

main()
