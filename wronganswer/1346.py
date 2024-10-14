from sys import stdin

def phi(n, songs, idSong):
    ans, L = 0, []
    for i in range(n): L.append((songs[i][0], songs[i][1]/songs[i][2]))
    L.sort(key=lambda x: x[1])
    ans = int(L[idSong-1][0])
    return ans

def main():
    input = stdin.readline()
    while input != '' and input != '\n':
        n = int(input)
        songs = []
        while len(songs) < n:
            s = list(map(float, stdin.readline().split()))
            for i in range(0, len(s)-1, 3): songs.append((s[i], s[i+1], s[i+2]))
        idSong = int(stdin.readline())
        print(phi(n, songs, idSong))
        input = stdin.readline()
main()           