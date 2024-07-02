import math
import sys

def SparseTable(array):
    n = len(array)
    st = [0] * n
    LOG_MAX = int(math.log2(n-1)) + 2
    # gcd_counter = [0] * (max(array)+1)
    for i in range(n):
        st[i] = [0] * (LOG_MAX)
        st[i][0] = array[i]
        # gcd_counter[array[i]]+=1
    for j in range(1, LOG_MAX):
        for i in range(n):
            if i + 2**(j)-1  >= n:
                break
            curr_gcd = math.gcd(st[i][j-1], st[i + 2**(j-1)][j-1])
            st[i][j] = curr_gcd
            # gcd_counter[curr_gcd]+=1
    # gcd_counter = [0] * (max(array)+1)
        
    
    def get(l, r):
        log = int(math.log2(r-l+1))
        if log != int(math.log(r-l+2)):
            return st[l][log]
        return math.gcd(st[l][log], st[r-2**log+1][log])


    def get_gcd_count(fixed_gcd):
        def BinSearch(num, l, r, interval_beg, sign_factor):
            m = 0
            while(l < r):
                m = (r-l)//2
                if (l-r)%2!=0: 
                    m -= 1
                if sign_factor == -1:
                    if get(interval_beg, m) <= num: r = m
                    else:                   l = m
                elif sign_factor == 1:
                    if get(interval_beg, m) >= num: l = m
                    else:                   r = m
            return l
        result = 0
        for l in range(n):
            r = l
            min_index = l
            max_index = l
            power = 0
            while(r < n):                       # Contemplar el caso en el que no haya coincidencia con ese especifico gcd.
                curr_gcd = get(l, r)
                if curr_gcd > fixed_gcd:
                    min_index = r
                    max_index = r
                elif curr_gcd == fixed_gcd:
                    max_index = min(r + 2**power, n)
                else:
                    if min_index == max_index:
                        return 0
                    break
                
                r = l+2**power
                power+=1
            result += BinSearch(fixed_gcd, min_index, max_index, l, sign_factor=1) - BinSearch(fixed_gcd, right=max_index, left=min_index, sign_factor=-1)

        return result
    
    # for l in range(n):
    #     for r in range(l, n):
    #         gcd_counter[get(l, r)] += 1

    return st, get, get_gcd_count
        
# st, get = SparseTable([1, 2, 3, 4, 5, 6])
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

    st, get, get_gdc_count = SparseTable(array)

    for q in queries:
        print(get_gdc_count(q))
        

    

if __name__ == "__main__":
    main()