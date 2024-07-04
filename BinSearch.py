def BinSearch(num, begin, sign_factor, get, n):
            l, r = begin, n-1
            last_index_found = -1
            
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

def main():
    array = [6, 5, 4, 4, 4, 4, 4, 4, 3, 2, 1]
    get = lambda a, b: array[b]
    print(BinSearch(4, 0, -1, get, len(array)))
    print(BinSearch(4, 0, 1, get, len(array)))

main()