from sys import stdin

def phi(students, studentsOrd, n):
    ans, i, j = 0, 0, 0
    while i < n and j < n:
        if students[i] == studentsOrd[j]:
            i += 1
            j += 1
        else:
            i += 1
            ans += 1
    return ans

def main():
    T = int(stdin.readline())
    for i in range(T):
        n = int(stdin.readline())
        students = list(map(int, stdin.readline().split()))
        studentsOrd = students.copy()
        studentsOrd.sort()
        print(f"Case {i+1}: {phi(students, studentsOrd, n)}")
main()