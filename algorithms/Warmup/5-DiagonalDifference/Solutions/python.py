def diagonalDifference(a):
    ultimaPosicao = len(a) - 1
    diagonalPrincipal = 0
    diagonalSecundaria = 0
    for x in range(len(a)):
        diagonalPrincipal = diagonalPrincipal + a[x][x]
        diagonalSecundaria = diagonalSecundaria + a[x][ultimaPosicao - x]
    return abs(diagonalPrincipal - diagonalSecundaria)
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
