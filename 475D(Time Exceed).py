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
        # if log != int(math.log(r-l+2)):
        #     return st[l][log]
        return math.gcd(st[l][log], st[r-2**log+1][log])


    def get_gcd_count(fixed_gcd):
        def BinSearch(num, begin, sign_factor):
            l, r = begin, n-1
            last_index_found = -1
            m=0
            while(l < r):
                m=(l+r)//2
                beg_to_m_gcd = get(begin, m)
                if beg_to_m_gcd == num:
                    last_index_found = m
                    
                if sign_factor == -1:
                    if beg_to_m_gcd <= num:
                        r = m-1
                    else:
                        l = m+1
                elif sign_factor == 1:
                    if beg_to_m_gcd >= num:
                        l = m+1
                    else:
                        r = m-1
            if l==r and get(begin, r)==num: last_index_found=r
            return last_index_found

        result = 0
        for l in range(n):
            forward_limit = BinSearch(fixed_gcd, l, 1)
            if forward_limit == -1:
                continue
            backward_limit = BinSearch(fixed_gcd, l, -1)
            result += forward_limit - backward_limit + 1
        return result

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
        # print(f"gcd={q}: {get_gdc_count(q)} veces")

        

    

if __name__ == "__main__":
    main()