import math
import sys

def SpTa(array):
    n = len(array)
    st = [0] * n
    LOG_MAX = int(math.log2(n-1)) + 1
    for k in range(n):
        st[k] = [0] * LOG_MAX
    gcd_counter = [0] * max(array)
    for j in range(LOG_MAX):
        for i in range(n):
            if i + 2**j - 1 >= n:
                break
            if j == 0:
                st[i][j] = array[i]
                continue
            curr_gcd = math.gcd(st[i][j-1], st[i + 2**(j)-1][j-1])
            st[i][j] = curr_gcd
            gcd_counter[curr_gcd]+=1

    # for i in range(n):
    #     gcd_counter[st[i][LOG_MAX-1]]+=1
        
    return gcd_counter

# st, get = SpTa([1, 2, 3, 4, 5, 6])
# print(st)
# print(math.gcd(1, 2))

def main():
    input = sys.stdin.buffer.readline

    firstline = input().strip().split()
    secondline = input().strip().split()
    thirdline = input().strip().split()
    n = int(firstline[0])
    q = int(thirdline[0])
    array = [int(item) for item in secondline]

    queries = []
    for i in range(q):
        queries.append(int(input().strip()))

    gcd_counter = SpTa(array)
    for q in queries:
        if q >= len(gcd_counter):
            print(0)
            continue
        print(gcd_counter[q])

    

if __name__ == "__main__":
    main()