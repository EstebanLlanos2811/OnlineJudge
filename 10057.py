from sys import stdin

def binarySearchLeft(A, x):
    low, hi = 0, len(A) - 1
    while low <= hi:
        mid = low + ((hi - low) >> 1)
        if A[mid] < x: low = mid + 1
        else: hi = mid - 1
    return low

def binarySearchRight(A, x):
    low, hi = 0, len(A) - 1
    while low <= hi:
        mid = low + ((hi - low) >> 1)
        if A[mid] <= x: low = mid + 1
        else: hi = mid - 1
    return hi    

def main():
    inp = stdin.readline()
    while inp != '' and inp != '\n':
        T = int(inp)
        A = []
        for _ in range(T): A.append(int(stdin.readline()))
        A.sort()
        n = len(A)
        mid = (n - 1) >> 1
        if n % 2 == 0:
            res1 = A[mid]
            if A[mid] == A[mid + 1]: res2 = (binarySearchRight(A, A[mid]) - binarySearchLeft(A, A[mid])) + 1
            else:
                res2 = (binarySearchRight(A, A[mid]) - binarySearchLeft(A, A[mid])) + 1
                res2 += (binarySearchRight(A, A[mid + 1]) - binarySearchLeft(A, A[mid + 1])) + 1
            res3 = (A[mid + 1] - A[mid]) + 1
        else:
            res1 = A[mid]
            res2 = ((binarySearchRight(A, A[mid]) - binarySearchLeft(A, A[mid])) + 1)
            res3 = 1
        print(res1, res2, res3)
        inp = stdin.readline()

main()