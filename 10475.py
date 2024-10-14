from sys import stdin

words, prohi, S, sols = None, None, None, None

def conflict(A, w):
    ans = True
    for i in range(len(A)):
        if (A[i], w) in prohi or (w, A[i]) in prohi: ans = False
    return ans

def solve(n, A):
    global sols
    if len(A) == S: print(' '.join(A)) 
    else:
        k = n
        while k < len(words):
            if len(A) < S and words[k] not in A and conflict(A, words[k]):
                A.append(words[k])
                solve(k + 1, A)
                A.pop()
            k += 1
            
def main():
    global words, prohi, S, sols
    cases = int(stdin.readline())
    for i in range(cases):
        T, P, S = map(int, stdin.readline().split())
        words, prohi, A = [], [], []
        for _ in range(T):
            topic = stdin.readline().strip()
            words.append(topic.upper())
        for _ in range(P):
            w1, w2 = stdin.readline().split()
            prohi.append((w1.upper(), w2.upper()))
        words.sort(key=lambda x: (-len(x), x))
        sols = []
        print(f'Set {i+1}:')
        solve(0, A)
        print()
        words, prohi, S, sols = None, None, None, None
main()
