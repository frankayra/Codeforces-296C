import math
from collections import defaultdict

# Función para calcular el GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Construcción de la Sparse Table
def buildSparseTable(arr, n):
    log = [0] * (n + 1)
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1

    K = log[n] + 1
    st = [[0] * K for _ in range(n)]

    for i in range(n):
        st[i][0] = arr[i]

    j = 1
    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) - 1) < n:
            st[i][j] = gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1

    return st, log

# Función para obtener el GCD de un subarreglo [L, R]
def queryGCD(L, R, st, log):
    j = log[R - L + 1]
    return gcd(st[L][j], st[R - (1 << j) + 1][j])

# Función principal
def solve(arr, queries):
    n = len(arr)
    st, log = buildSparseTable(arr, n)
    
    result = []
    for x in queries:
        gcdCount = defaultdict(int)
        
        i = 0
        while i < n:
            j = i
            currentGCD = arr[i]
            while j < n:
                currentGCD = queryGCD(i, j, st, log)
                gcdCount[currentGCD] += 1
                if currentGCD < x:
                    break
                j += 1
            i += 1
        
        result.append(gcdCount[x])
    
    return result

# Lectura de entrada y llamada a la función principal
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    arr = [int(data[idx + i]) for i in range(n)]
    idx += n
    q = int(data[idx])
    idx += 1
    queries = [int(data[idx + i]) for i in range(q)]
    
    results = solve(arr, queries)
    
    for res in results:
        print(res)