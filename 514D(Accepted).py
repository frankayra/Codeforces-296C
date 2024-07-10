import math
import sys

def SparseTable(array, m, k_shoots):
    n = len(array)

    # st = [0] * n
    # LOG_MAX = int(math.log2(n-1)) + 2
    LOG_MAX = int(math.log2(n)) + 1
    st = [[[0]*m for _ in range(LOG_MAX)] for _ in range(n)]
    for i in range(n):
        for k in range(m):
            st[i][0][k] = array[i][k]
    for j in range(1, LOG_MAX):
        for i in range(n):
            if i + 2**(j)-1  >= n:
                break
            for k in range(m):
                curr_max = max(st[i][j-1][k], st[i + 2**(j-1)][j-1][k])
                st[i][j][k] = curr_max
        
    
    def get(l, r):
        log = int(math.log2(r-l+1))
        left_segment = st[l][log]
        right_segment = st[r-2**log+1][log]
        return sum((max(left_segment[i], right_segment[i]) for i in range(m)))
        # return max(left_sum, right_sum)


    def get_max_interval():
        def BinSearch(shoots, begin, lim_poda):
            l, r = begin, n-1
            last_index_found = -1
            m=0
            while(l < r):
                m=(l+r)//2
                beg_to_m_max_consum = get(begin, m)
                if beg_to_m_max_consum <= shoots:
                    last_index_found = m
                    l = m+1
                else:
                    r = m-1
                    if r - begin < lim_poda: return -1
                    
            if l==r and get(begin, r)<=shoots: last_index_found=r
            return last_index_found

        result_left = -1
        result_right = -1
        lim_poda = 0
        for l in range(n):
            if n-l < lim_poda: break
            forward_limit = BinSearch(k_shoots, l, lim_poda)
            # if forward_limit == -1:
            #     continue
            if lim_poda > forward_limit-l: continue
            lim_poda = forward_limit - l
            result_left = l
            result_right = forward_limit
        return result_left, result_right

    return st, get, get_max_interval
        

def main():
    input = sys.stdin.buffer.readline

    firstline = input().strip().split()
    n = int(firstline[0])
    m = int(firstline[1])
    k = int(firstline[2])

    array = []
    for i in range(n):
        array.append([int(a) for a in input().strip().split()])

    st, get, get_max_interval = SparseTable(array, m, k)

    best_interval = get_max_interval()
    l, r = best_interval[0], best_interval[1]
    
    log = int(math.log2(r-l+1))
    left_segment = st[l][log]
    right_segment = st[r-2**log+1][log]
    for i in range(m):
        if l == -1 or r == -1:
            for k in range(m):
                print(0, end=" " if k != m-1 else "")
            break
        print(max(left_segment[i], right_segment[i]), end=" " if i != m-1 else "")
    
        

        

    

if __name__ == "__main__":
    main()