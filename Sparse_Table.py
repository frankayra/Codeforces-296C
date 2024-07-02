import math
import sys

def SpTa(array):
    n = len(array)
    st = [0] * n
    LOG_MAX = int(math.log2(n-1)) + 2
    gcd_counter = [0] * (max(array)+1)
    for i in range(n):
        st[i] = [0] * (LOG_MAX)
        st[i][0] = array[i]
        gcd_counter[array[i]]+=1
    for j in range(1, LOG_MAX):
        for i in range(n):
            # st[n-1][j] = array[n-1]
            if i + 2**(j)-1  >= n:
                break
            curr_gcd = math.gcd(st[i][j-1], st[i + 2**(j-1)][j-1])
            st[i][j] = curr_gcd
            gcd_counter[curr_gcd]+=1

    def get(l, r):
        log = int(math.log2(r-l+1))
        return math.gcd(st[l][log], st[r-2**log+1][log])
    
    return st, get, gcd_counter

st, get, gcd_counter = SpTa([2, 6, 3])
print(f"st: {st}")
print([f"{i}({gcd_counter[i]})"for i in range(len(gcd_counter))])
# print(math.gcd(1, 2))
print(get(0, 2))
