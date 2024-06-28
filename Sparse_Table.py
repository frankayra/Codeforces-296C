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

    def get(l, r):
        log = int(math.log2(r-l+1))
        return math.gcd(st[l][log], st[r-2**log+1][log])
    
    return st, get

st, get = SpTa([2, 2, 3, 4, 5, 6])
print(st)
# print(math.gcd(1, 2))
